from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone

def now_utc():
    return datetime.now(timezone.utc)

class Message(BaseModel):
    role: str
    content: str
    timestamp: datetime = Field(default_factory=now_utc)

class Conversation(BaseModel):
    id: str
    user_id: str
    messages: List[Message] = []
    created_at: datetime = Field(default_factory=now_utc)
    updated_at: datetime = Field(default_factory=now_utc)

class Ticket(BaseModel):
    id: str
    user_id: str
    department: str
    priority: str
    status: str = "open"
    subject: str
    description: str
    created_at: datetime = Field(default_factory=now_utc)
