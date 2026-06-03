# AI Financial Chatbot Backend

This project is a FastAPI-based backend for a document-aware financial chatbot. Users can upload PDF documents and ask questions about their contents. The system extracts text from uploaded PDFs, generates embeddings, stores them in a FAISS vector database, and retrieves relevant context to answer user queries using a Groq-hosted LLM.

## Features

* User signup and login
* PDF upload and text extraction
* Text chunking and embedding generation
* FAISS-based semantic search
* Context-aware question answering
* Financial assistant focused on mutual fund and financial documents

## Technology Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* pypdf
* sentence-transformers
* FAISS
* Groq (Llama 3.3 70B Versatile)
* python-dotenv
## API EndPoints
<img width="425" height="282" alt="image" src="https://github.com/user-attachments/assets/b49b431e-a412-407b-9f9b-c7a5cb1fbb0d" />


## How It Works

1. A user uploads a PDF document.
2. Text is extracted from the PDF.
3. The text is split into smaller chunks.
4. Embeddings are generated for each chunk.
5. Embeddings are stored in a FAISS index.
6. When a question is asked, the system retrieves the most relevant chunks.
7. Retrieved context and the user's question are sent to the language model.
8. The model generates an answer based primarily on the uploaded document.

## Setup

Create a virtual environment:


python -m venv myenv


Activate it:


myenv\Scripts\activate


Install dependencies:


pip install -r app/requirements.txt


Create a `.env` file:


GROQ_API_KEY=your_groq_api_key


Run the application:


uvicorn app.main:app --reload


## Notes

* Uploaded document embeddings are stored in a FAISS index.
* User data is stored in SQLite.
* Responses are designed to use document context before relying on general financial knowledge.
* This project is intended for educational and informational use and should not be considered a source of investment advice.

🎯 Future Enhancements
Multi-document support
Conversation memory
User-specific document storage
Advanced financial analytics
Cloud database integration
Role-based access control
Deployment with Docker
📄 License

This project is intended for educational and development purposes.

🌟 Final Thoughts

AI Financial Chatbot Backend demonstrates how FastAPI, semantic search, vector databases, and large language models can be combined to create a powerful document-grounded financial assistant capable of answering questions based on uploaded financial documents.
