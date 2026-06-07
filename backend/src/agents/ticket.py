from src.graph.state import AgentState
import logging
import uuid
from datetime import datetime, timezone

log = logging.getLogger(__name__)

def ticket_agent_node(state: AgentState):
    log.info("Creating support ticket...")
    
    intent = state.get("intent", "Inquiry")
    if intent in ["Inquiry", "Pricing"]:
        # No ticket needed for simple questions
        return {"ticket_info": None}
        
    ticket_id = f"SUP-2026-{str(uuid.uuid4())[:4].upper()}"
    department = state.get("department", "Support")
    
    ticket_data = {
        "id": ticket_id,
        "department": department,
        "priority": "Medium",
        "status": "Open",
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    # Save to database logic goes here
    
    return {"ticket_info": ticket_data}
