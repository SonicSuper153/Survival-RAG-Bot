
# 🛡️ Survival Guide LLM (Offline RAG Chatbot)

An **offline Retrieval-Augmented Generation (RAG) chatbot** designed for survival scenarios where internet access may be unavailable. The system combines **local LLM inference** with a **vector-based retrieval pipeline** for accurate, context-aware Q\&A.

---

## 🚀 Features

* **Offline LLM Inference** using [Ollama](https://ollama.ai) with `gpt-oss:20b`
* **Embeddings** generated with `nomic-embed-text:v1.5`
* **Custom VectorDB** for efficient document retrieval
* **Document Ingestion** and **Text Chunking** for knowledge base creation
* **Agent-based Architecture** for modularity and scalability
* **Python CLI** for querying and structured outputs
* **No Internet Required** 

---

## 🏗️ Tech Stack

* **Language**: Python 3.10+
* **LLM**: [Ollama](https://ollama.ai) (`gpt-oss:20b`)
* **Embeddings**: `nomic-embed-text:v1.5`
* **Vector Database**: Custom implementation using FAISS-like approach
* **APIs**: OpenAI API (for embedding generation, if required)
* **CLI Interface**: Built-in for user queries and responses

---

## ⚡ How It Works

1. **Document Ingestion**
   Load survival guides or reference docs into the system.

2. **Embedding Generation**
   Convert text chunks into vector embeddings using `nomic-embed-text:v1.5`.

3. **Vector Storage**
   Store embeddings in the custom VectorDB for fast similarity search.

4. **Query Processing**
   Accept user queries via CLI → retrieve context → generate response with Ollama (`gpt-oss:20b`).

---

## ✅ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/survival-rag-chatbot.git
cd survival-rag-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install [Ollama](https://ollama.ai)

Follow official instructions for your OS.

### 4. Pull the model

```bash
ollama pull gpt-oss:20b
```

---

## ▶️ Usage

### Initialize VectorDB

```bash
python main.py --init-db data/
```

### Ask Questions

```bash
python main.py --query "How to purify water in the wild?"
```

---

## 📌 Example Query

**User:**
`How to start a fire without matches?`

**Chatbot:**
"To start a fire without matches, gather dry tinder, use a flint and steel or friction method like a bow drill. Ensure proper ventilation and gradually add larger sticks."

---

## 🔮 Future Enhancements

* GUI interface (React or Streamlit)
* Integration with voice input/output
* Multi-document semantic search
* Offline embedding generation (using local models)

---
