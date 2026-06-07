from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from src.db.models import Message, Ticket

from src.graph.workflow import build_workflow
from langchain_core.messages import HumanMessage

router = APIRouter()
graph = build_workflow()

class ChatRequest(BaseModel):
    message: str
    user_id: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str
    conversation_id: str
    ticket_created: bool = False
    ticket_id: Optional[str] = None

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    # Construct state
    state = {
        "messages": [HumanMessage(content=req.message)],
        "intent": None,
        "department": None,
        "is_duplicate": False,
        "cached_response": None,
        "ticket_info": None,
        "final_response": None,
        "metrics": {}
    }
    
    # Run LangGraph workflow
    result = graph.invoke(state)
    
    ticket_info = result.get("ticket_info", {})
    return ChatResponse(
        reply=result.get("final_response", "Error generating response."),
        conversation_id=req.conversation_id or "new_conv_123",
        ticket_created=bool(ticket_info),
        ticket_id=ticket_info.get("id") if ticket_info else None
    )

@router.get("/tickets/{user_id}", response_model=List[Ticket])
async def get_tickets(user_id: str):
    # Mock return for now
    return []
