import os
from brain import Brain
from tools.databaseUtils import ChromaPipeline
from tools.fileReader import FileReader
from agents import Agent

class Find:
    def __init__(self):
        self.brain = Brain()
        self.tool1 = ChromaPipeline()   # instantiate the class
        self.tool2 = FileReader()      # instantiate the class
        self.agent1 = Agent()

    def vectorDB_folder_books(self, pdf_folder: str):
        self.pdf_folder = pdf_folder

        books_folder = r"C:\Users\Ishmeet\OpenAI\tools\texts"
        db_folder = r"C:\Users\Ishmeet\OpenAI\tools\db"

        print("[STEP 2] Building/Updating Vector DB...")
        chroma_pipeline = self.tool1.initialize_vector_store_forall()

        print("[SUCCESS] PDFs processed and vector DB ready for RAG!")

    def vectorDB_folder(self, pdf_folder: str):
        self.pdf_folder = pdf_folder

        books_folder = r"C:\Users\Ishmeet\OpenAI\tools\texts"
        db_folder = r"C:\Users\Ishmeet\OpenAI\tools\db"

        print("[STEP 1] Converting PDFs to text...")
        file_reader = FileReader(output_dir=books_folder)
        file_reader.convert_folder_pdfs(self.pdf_folder)

        print("[STEP 2] Building/Updating Vector DB...")
        chroma_pipeline = self.tool1.initialize_vector_store_forall(books_dir=books_folder, db_dir=db_folder)

        print("[SUCCESS] PDFs processed and vector DB ready for RAG!")

    def vectorDB_initialize(self, pdf: str):
        text_file = self.tool2.pdf_to_txt(pdf)  # convert PDF → TXT
        self.tool1.initialize_vector_store_forone(text_file)  # add to vector DB
    
    def one_query(self, query: str) -> str:
        print(f"Searching for: {query}\n")
        retriever = self.tool1.get_retriever()  
        results = retriever.invoke(query)       
        return results
    
    def structured_output(self, query: str) -> str:
        results = self.one_query(query)
        context_texts = "\n\n".join([doc.page_content for doc in results])
        agent = Agent()
        return agent.output(query,context_texts)


    