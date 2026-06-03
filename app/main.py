
from app.services.llm_service import ask_llm

# print(ask_llm("What is SIP?", ""))
from fastapi import FastAPI
import app.database as db

Base = db.Base
engine = db.engine

# ✅ correct imports
from app.routers import chat, upload, auth

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# ✅ include ALL routers
app.include_router(chat.router)
app.include_router(auth.router)   # 🔥 THIS LINE MUST EXIST

from dotenv import load_dotenv

load_dotenv()  # load once globally
