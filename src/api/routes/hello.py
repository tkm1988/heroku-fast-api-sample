from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", name="tags:get-hello")
async def hello():
    return {"message": "server hello"}
