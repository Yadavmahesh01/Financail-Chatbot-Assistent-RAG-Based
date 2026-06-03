from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_reader import read_pdf
from app.utils.text_chunker import split_text
from app.services.embedding_service import create_embeddings
from app.services.vector_store import store_embeddings

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"uploaded_pdfs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    print("Processing uploaded document...")

    text = read_pdf(file_path)

    if not text:
        return {"error": "No text extracted"}

    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    store_embeddings(embeddings, chunks)

    return {"message": "Document processed successfully"}