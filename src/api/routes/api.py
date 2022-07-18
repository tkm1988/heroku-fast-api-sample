from fastapi import APIRouter
from src.api.routes import hello

router = APIRouter()

router.include_router(hello.router, tags=["hello"], prefix="")
