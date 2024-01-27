from fastapi import FastAPI

from .config import settings
from .db.engine import Base, SessionLocal, engine
from .endpoints.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(api_router)
