# Project Structure and Modules

This document provides a full breakdown of the backend structure, code modules, and frontend setup.

## 1. Backend Workflow (`backend/src/graph/workflow.py`)
The core of the AI Service Desk is a state machine built with **LangGraph**. The state is passed through multiple specialized AI Agents (Nodes):

1. **Intent Analyzer** (`agents/intent.py`): Determines the core intent (Inquiry, Bug, Feature Request, Pricing, Complaint).
2. **Department Router** (`agents/router.py`): Routes the request to the specific department (Sales, Tech Support, Marketing, etc.).
3. **Duplicate Detection** (`agents/duplicate.py`): Checks the MongoDB Vector DB for >90% semantic similarity to prevent redundant LLM calls. *(Currently a stub)*
4. **Knowledge Agent** (`agents/knowledge.py`): Uses RAG to fetch contextual company documentation. *(Currently a stub)*
5. **Ticket Agent** (`agents/ticket.py`): Conditionally generates a formatted `SUP-2026-XXXX` support ticket if the issue warrants one.
6. **Response Agent** (`agents/response.py`): Compiles the ticket info, the knowledge context, and intent into a cohesive, helpful reply using the primary LLM.
7. **Analytics Agent** (`agents/analytics.py`): Logs token usage and estimated cost to the MongoDB tracking collections.

## 2. Code Modules (`backend/src/`)
- `api/routes.py`: Contains the `/api/chat` FastAPI endpoint that constructs the initial `AgentState` and triggers the LangGraph `invoke()` method.
- `db/database.py`: Establishes the asynchronous Motor MongoDB connection.
- `db/models.py`: Defines the Pydantic schemas for `Message`, `Conversation`, and `Ticket` data structures.
- `agents/*.py`: Individual Node implementations containing `ChatPromptTemplate` logic connected to local Ollama models.

## 3. Frontend Architecture (`frontend/`)
The frontend is a Next.js App Router application implementing a premium AI support interface.

- **`app/chat/page.tsx`**: The customer-facing chat UI communicating with the FastAPI `/api/chat` endpoint.
- **`app/tickets/page.tsx`**: An internal dashboard for Support Agents to view and manage tickets created by the AI.
- **`app/analytics/page.tsx`**: A dashboard displaying system metrics (costs saved via caching, token usage, top intents).
