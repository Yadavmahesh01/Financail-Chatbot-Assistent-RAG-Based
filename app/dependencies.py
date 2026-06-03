from fastapi import Header, HTTPException
from jose import jwt
from app.database import SessionLocal
from app.models import User
from app.auth_utils import SECRET_KEY, ALGORITHM

def get_current_user(token: str = Header(...)):
    db = SessionLocal()

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = db.query(User).filter(User.email == payload["sub"]).first()
        return user
    except:
        raise HTTPException(status_code=401, detail="Invalid token")