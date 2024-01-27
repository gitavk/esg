from fastapi import FastAPI

from .config import settings
from .db.engine import Base, engine
from .endpoints.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(api_router)
