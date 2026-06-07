from langgraph.graph import StateGraph, START, END
from src.graph.state import AgentState
from src.agents.intent import intent_analyzer_node
from src.agents.router import department_router_node
from src.agents.duplicate import duplicate_detection_node
from src.agents.knowledge import knowledge_agent_node
from src.agents.ticket import ticket_agent_node
from src.agents.response import response_agent_node
from src.agents.analytics import analytics_agent_node
import logging

log = logging.getLogger(__name__)

def build_workflow():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("intent_analyzer", intent_analyzer_node)
    workflow.add_node("department_router", department_router_node)
    workflow.add_node("duplicate_detection", duplicate_detection_node)
    workflow.add_node("knowledge_agent", knowledge_agent_node)
    workflow.add_node("ticket_agent", ticket_agent_node)
    workflow.add_node("response_agent", response_agent_node)
    workflow.add_node("analytics_agent", analytics_agent_node)
    
    # Add edges
    workflow.add_edge(START, "intent_analyzer")
    workflow.add_edge("intent_analyzer", "department_router")
    workflow.add_edge("department_router", "duplicate_detection")
    
    # Conditional edge on duplicate detection
    def route_duplicate(state: AgentState):
        if state.get("is_duplicate"):
            return "response_agent"
        return "knowledge_agent"
        
    workflow.add_conditional_edges("duplicate_detection", route_duplicate)
    
    workflow.add_edge("knowledge_agent", "ticket_agent")
    workflow.add_edge("ticket_agent", "response_agent")
    workflow.add_edge("response_agent", "analytics_agent")
    workflow.add_edge("analytics_agent", END)
    
    return workflow.compile()
