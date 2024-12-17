from fastapi import APIRouter, Request
from LLMCloud.models.models import LoadRequestModel
from LLMCloud.app import app

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Welcome to LLM Cloud!"}


@router.post("/load_model/")
async def load_model(request: LoadRequestModel):
    model_name = request.model_name
