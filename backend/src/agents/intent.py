from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from src.graph.state import AgentState
import os
import logging

log = logging.getLogger(__name__)

class IntentClassification(BaseModel):
    intent: str = Field(description="The core intent of the user message (e.g., Inquiry, Bug, Feature Request, Pricing, Complaint)")

def intent_analyzer_node(state: AgentState):
    messages = state.get("messages", [])
    if not messages:
        return {"intent": "Unknown"}
    
    last_message = messages[-1].content
    
    model_name = os.getenv("OLLAMA_PRIMARY_MODEL", "qwen3.5:4b")
    llm = ChatOllama(model=model_name, temperature=0, base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))
    llm_with_struct = llm.with_structured_output(IntentClassification)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert intent analyzer for TrNe Tech Solutions AI Service Desk. "
                   "Determine the intent of the user's message. Possible intents: Inquiry, Bug, Feature Request, Pricing, Complaint."),
        ("user", "{message}")
    ])
    
    chain = prompt | llm_with_struct
    try:
        result = chain.invoke({"message": last_message})
        intent = result.intent
        log.info(f"Detected intent: {intent}")
    except Exception as e:
        log.error(f"Error in intent analysis: {e}")
        intent = "Inquiry" # Default fallback
    
    return {"intent": intent}
