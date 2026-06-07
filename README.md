# TrNu Tech Solutions AI Service Desk

## Project Vision
An Enterprise-grade AI Service Desk Platform acting as the intelligent first point of contact for all customer support.
This system autonomously routes requests, handles basic inquiries, detects duplicates, creates tickets, reduces AI costs through semantic caching, and stores all conversation and metric history. It heavily relies on **LangGraph**, **LangChain**, and local **Ollama** models.

---

## 🎯 Main Goal & Workflow
When a customer sends a message:
1. **User Message** is received by the backend.
2. **AI Agent analyzes intent** (Inquiry, Bug, Feature Request, Pricing, Complaint).
3. **Classifies department** (Sales, Technical, Marketing, etc.).
4. **Detects duplicates** (Semantic Similarity checks).
5. **Retrieves knowledge** via RAG.
6. **Creates a ticket** for the relevant department.
7. **Responds to customer** natively.
8. **Routes request internally** and logs analytics (Tokens, Cost, Latency).

---

## 🏢 Department Routing
The AI automatically assigns the user's issue to the appropriate team based on message context:
- **Marketing Team**: Services, technology stack, general software projects, meetings.
- **Sales Team**: Pricing, quotations, subscriptions, SaaS purchases.
- **Technical Support Team**: Application crashes, login issues, API errors, DB errors.
- **Development Team**: New features, product enhancements, change requests.
- **Cloud Team**: AWS, GCP, Docker, Kubernetes deployments.

---

## 🧠 LangGraph Architecture
The system employs a sophisticated `StateGraph` workflow defined in `backend/src/graph/workflow.py`:

1. **Intent Analyzer** (`Node 1`): Detects the exact intent of the message.
2. **Department Router** (`Node 2`): Selects the destination team based on the intent.
3. **Duplicate Detection Agent** (`Node 3`): Matches against existing issues in the semantic cache. Avoids LLM calls if Similarity > 90%.
4. **Knowledge Agent** (`Node 4`): Queries company documents (FAQ, Product/Service/Pricing Docs).
5. **Ticket Agent** (`Node 5`): Generates a localized `SUP-2026-XXXX` styled ticket if the user intent warrants escalation.
6. **Response Agent** (`Node 6`): Combines all state information (Context, Ticket, Intent) to provide a tailored response.
7. **Analytics Agent** (`Node 7`): Traces metrics such as estimated token cost and execution latency.

---

## 💾 Cost Optimization & Features
- **Semantic Cache**: Avoids repeated generation for identical or highly similar questions (>90% match).
- **Prompt Compression**: Selectively forwards the last 5 messages rather than full history to optimize context window limits.
- **Model Selection Strategy**:
    - `gemma4:e4b` for simple/fast routing tasks.
    - `qwen3.5:4b` for complex business queries.
    - `qwen2.5-coder:3b` for code-specific analysis.

---

## 🚀 Running the Project

### Prerequisites
1. **Ollama**: Must be running locally on `http://localhost:11434`. Ensure the required models are pulled:
   ```bash
   ollama run qwen3.5:4b
   ollama run gemma4:e4b
   ```
2. **MongoDB**: Have a local or Atlas MongoDB connection ready. Update the `.env` file accordingly.

### 1. Backend (FastAPI + Python)
Built with Python, FastAPI, and `uv` package manager.

```bash
cd backend
# Run the FastAPI server natively using uv (no manual activation needed)
uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

# (Optional) To manually activate in PowerShell: .venv\Scripts\Activate.ps1
```
View the interactive API Swagger documentation at `http://localhost:8000/api/docs`.
For detailed API request payloads and Postman setup, see [`docs/api_documentation.md`](docs/api_documentation.md).

### 2. Frontend (Next.js)
Built with React, Next.js (App Router), TailwindCSS, ShadCN UI, Recharts, and TanStack Query.

```bash
cd frontend
# Install dependencies
npm install
# Start the development server
npm run dev
```
Visit `http://localhost:3000` to interact with the customer portal and agent dashboard.

---

## 📂 Folder Structure Map

```text
/
├── backend/
│   ├── .env
│   ├── requirements.txt
│   └── src/
│       ├── main.py                 # FastAPI Entry Point
│       ├── api/
│       │   └── routes.py           # /api/chat router triggering LangGraph
│       ├── agents/                 # LangGraph Nodes
│       │   ├── intent.py
│       │   ├── router.py
│       │   ├── knowledge.py
│       │   ├── duplicate.py
│       │   ├── ticket.py
│       │   ├── response.py
│       │   └── analytics.py
│       ├── graph/
│       │   ├── state.py            # TypedDict defining memory state
│       │   └── workflow.py         # StateGraph Compilation
│       ├── db/                     # Motor MongoDB logic
│       └── rag/                    # Vector Embeddings
└── frontend/
    ├── .env
    ├── package.json
    └── app/                        # Next.js App Router Structure
        ├── chat/                   # Customer facing interface
        ├── tickets/                # Support dashboard interface
        └── analytics/              # Metrics dashboard interface
```

---

## 🛠 Technology Stack
- **Backend**: Python, FastAPI, Uvicorn, LangGraph, LangChain, Motor (MongoDB), Sentence-Transformers, Numpy.
- **Frontend**: Next.js, React, TailwindCSS, Recharts, ShadCN UI, TanStack Query.
- **AI/Local**: Ollama (`qwen3.5:4b`, `gemma4:e4b`).
