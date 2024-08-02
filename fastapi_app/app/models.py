from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    id: str
    author: str
    text: str

class MessageCreate(BaseModel):
    author: str
    text: str