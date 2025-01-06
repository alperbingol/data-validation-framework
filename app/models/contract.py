from pydantic import BaseModel
from typing import Dict, Any

class DataContract(BaseModel):
    name: str
    description: str
    schema: Dict[str, Any]