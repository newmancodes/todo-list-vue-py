from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
async def read_example():
    return {"message": "This is an example endpoint."}

@router.post("/example")
async def create_example(item: dict):
    return {"message": "Example item created.", "item": item}