from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class LoadRequestModel(BaseModel):
    model_name: str
