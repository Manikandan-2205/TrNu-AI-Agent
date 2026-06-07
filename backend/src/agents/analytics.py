from src.graph.state import AgentState
import logging

log = logging.getLogger(__name__)

def analytics_agent_node(state: AgentState):
    log.info("Logging analytics and cost metrics...")
    
    # Placeholder for calculating token counts and cost
    # Usually we'd use a callback handler to get exact token usage
    
    messages = state.get("messages", [])
    if not messages:
        return {"metrics": {}}
        
    metrics = {
        "tokens": len(messages[-1].content) // 4,  # rough estimate
        "estimated_cost": 0.0, # Local LLMs are free, but we might track compute cost
        "model": "qwen3.5:4b"
    }
    
    return {"metrics": metrics}
