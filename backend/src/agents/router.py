from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from src.graph.state import AgentState
import os
import logging

log = logging.getLogger(__name__)

class DepartmentClassification(BaseModel):
    department: str = Field(description="The department to route to (e.g., Marketing, Sales, Technical Support, Development, Cloud Operations)")

def department_router_node(state: AgentState):
    messages = state.get("messages", [])
    if not messages:
        return {"department": "Technical Support"}
        
    last_message = messages[-1].content
    intent = state.get("intent", "Unknown")
    
    model_name = os.getenv("OLLAMA_PRIMARY_MODEL", "qwen3.5:4b")
    llm = ChatOllama(model=model_name, temperature=0, base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))
    llm_with_struct = llm.with_structured_output(DepartmentClassification)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert department router for TrNe Tech Solutions AI Service Desk. "
                   "Based on the user's message and the intent '{intent}', determine the destination department. "
                   "Options: Marketing, Sales, Technical Support, Development, Cloud Operations."),
        ("user", "{message}")
    ])
    
    chain = prompt | llm_with_struct
    try:
        result = chain.invoke({"intent": intent, "message": last_message})
        department = result.department
        log.info(f"Routed to department: {department}")
    except Exception as e:
        log.error(f"Error in department routing: {e}")
        department = "Technical Support" # Default fallback
    
    return {"department": department}
