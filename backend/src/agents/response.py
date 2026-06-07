from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from src.graph.state import AgentState
import os
import logging

log = logging.getLogger(__name__)

def response_agent_node(state: AgentState):
    log.info("Generating final response...")
    
    messages = state.get("messages", [])
    if not messages:
        return {"final_response": "Hello! How can I help you?"}
        
    last_message = messages[-1].content
    intent = state.get("intent", "Inquiry")
    dept = state.get("department", "Support")
    ticket_info = state.get("ticket_info")
    cached_response = state.get("cached_response")
    
    if cached_response:
        return {"final_response": cached_response}
        
    model_name = os.getenv("OLLAMA_PRIMARY_MODEL", "qwen3.5:4b")
    llm = ChatOllama(model=model_name, temperature=0.7, base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))
    
    system_prompt = f"""You are a helpful customer support AI agent for TrNe Tech Solutions.
The user's message has been classified as '{intent}' and routed to '{dept}'.
"""
    if ticket_info:
        system_prompt += f"A support ticket has been created. Ticket ID: {ticket_info['id']}."

    system_prompt += " Generate a polite and helpful final response."
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{message}")
    ])
    
    chain = prompt | llm
    
    try:
        result = chain.invoke({"message": last_message})
        final_response = result.content
    except Exception as e:
        log.error(f"Error generating response: {e}")
        final_response = "We received your message and will get back to you shortly."
        
    return {"final_response": final_response}
