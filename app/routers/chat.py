from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import embed_query
from app.services.vector_store import search_embeddings
from app.services.llm_service import ask_llm

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    query_embedding = embed_query(request.question)

    context = search_embeddings(query_embedding)

    context_text = " ".join(context)

    answer = ask_llm(request.question, context_text)

    return {"answer": answer}