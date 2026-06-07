from typing import TypedDict, List, Dict, Any, Optional
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: List[BaseMessage]
    intent: Optional[str]
    department: Optional[str]
    is_duplicate: bool
    cached_response: Optional[str]
    ticket_info: Optional[Dict[str, Any]]
    final_response: Optional[str]
    metrics: Dict[str, Any]
