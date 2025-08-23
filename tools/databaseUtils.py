import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings.base import Embeddings
from brain import Brain
from chromadb.config import Settings
from langchain_chroma import Chroma
from .fileReader import FileReader

class BrainEmbeddings(Embeddings):
    def __init__(self):
        self.brain = Brain()

    def embed_documents(self, texts):
        return [self.brain.getEmbeddings(text) for text in texts]

    def embed_query(self, text):
        return self.brain.getEmbeddings(text)


class ChromaPipeline:
    def __init__(self, books_dir=None, db_dir=None):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.books_dir = books_dir or os.path.join(current_dir, "texts")
        self.db_dir = db_dir or os.path.join(current_dir, "db")
        self.persistent_directory = os.path.join(self.db_dir, "chroma_db_with_metadata")
        self.embeddings = BrainEmbeddings()
        self.chroma_settings = Settings(anonymized_telemetry=False)

    def initialize_vector_store_forall(self):
        if not os.path.exists(self.books_dir):
            raise FileNotFoundError(f"[ERROR] The directory {self.books_dir} does not exist.")

        book_files = [f for f in os.listdir(self.books_dir) if f.endswith(".txt")]
        if not book_files:
            raise FileNotFoundError("[ERROR] No .txt files found in the directory.")

        documents = []
        for book_file in book_files:
            file_path = os.path.join(self.books_dir, book_file)
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()
            for doc in docs:
                doc.metadata = {"source": book_file}
            documents.extend(docs)

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(documents)

        print(f"[INFO] Number of document chunks: {len(docs)}")

        if os.path.exists(self.persistent_directory):
            # Load existing vector store and add new documents
            db = self.load_vector_store()
            db.add_documents(docs)
            print(f"[INFO] Added {len(docs)} chunks to existing vector store.")
        else:
            # Create a new vector store
            db = Chroma.from_documents(
                docs,
                self.embeddings,
                persist_directory=self.persistent_directory,
                client_settings=self.chroma_settings
            )
            print(f"[INFO] Created new vector store with {len(docs)} chunks.")

        print("[SUCCESS] Vector store initialized and persisted!")


    def initialize_vector_store_forone(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"[ERROR] File {file_path} does not exist.")

        loader = TextLoader(file_path, encoding="utf-8")
        documents = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(documents)

        if os.path.exists(self.persistent_directory):
            db = self.load_vector_store()
            db.add_documents(docs)
            print(f"[INFO] Added {len(docs)} chunks to existing vector store.")
        else:
            db = Chroma.from_documents(
                docs,
                self.embeddings,
                persist_directory=self.persistent_directory,
                client_settings=self.chroma_settings
            )
            print(f"[INFO] Created new vector store with {len(docs)} chunks.")

    def load_vector_store(self):
        if not os.path.exists(self.persistent_directory):
            raise FileNotFoundError("[ERROR] Vector store does not exist. Initialize it first.")

        return Chroma(
            persist_directory=self.persistent_directory,
            embedding_function=self.embeddings,
            client_settings=self.chroma_settings
        )

    # ✅ Add this retriever method
    def get_retriever(self, k=3, score_threshold=0.2):
        db = self.load_vector_store()
        retriever = db.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"k": k, "score_threshold": score_threshold}
        )
        return retriever
