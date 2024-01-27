from fastapi import APIRouter

from .esg import router as esg_router

api_router = APIRouter()
api_router.include_router(esg_router)

__all__ = ["api_router"]
