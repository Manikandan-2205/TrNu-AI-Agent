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

@router.get("/dashboard/metrics")
async def get_dashboard_metrics(timeframe: str = "week"):
    # This simulates fetching dynamic data from MongoDB
    if timeframe == "month":
        return {
            "agent_activity": [
                {"name": "Week 1", "resolved": 120, "escalated": 15},
                {"name": "Week 2", "resolved": 150, "escalated": 20},
                {"name": "Week 3", "resolved": 180, "escalated": 10},
                {"name": "Week 4", "resolved": 200, "escalated": 5},
            ],
            "department_issues": [
                {"name": "Technical", "value": 400},
                {"name": "Sales", "value": 300},
                {"name": "Billing", "value": 200},
            ],
            "new_clients": 45,
            "tokens_saved": 150000
        }
    else:
        return {
            "agent_activity": [
                {"name": "Mon", "resolved": 20, "escalated": 2},
                {"name": "Tue", "resolved": 25, "escalated": 5},
                {"name": "Wed", "resolved": 30, "escalated": 1},
                {"name": "Thu", "resolved": 15, "escalated": 4},
                {"name": "Fri", "resolved": 40, "escalated": 2},
                {"name": "Sat", "resolved": 10, "escalated": 0},
                {"name": "Sun", "resolved": 5, "escalated": 0},
            ],
            "department_issues": [
                {"name": "Technical", "value": 85},
                {"name": "Sales", "value": 40},
                {"name": "Billing", "value": 20},
            ],
            "new_clients": 12,
            "tokens_saved": 32000
        }
