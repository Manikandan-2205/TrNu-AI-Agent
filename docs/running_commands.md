# Running the Platform

## 1. Backend (FastAPI + LangGraph)
The backend is built with Python and the `uv` package manager. It uses FastAPI for the server.

### Prerequisites
1. Ensure **Ollama** is running locally (usually on port 11434).
2. Ensure you have the models downloaded:
   ```bash
   ollama run qwen3.5:4b
   ```
3. Ensure **MongoDB** is running locally or you have an Atlas URI set in `backend/.env`.

### Running the Server
```bash
cd backend

# The recommended way using uv (automatically uses the virtual environment)
uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

# Alternatively, if you want to manually activate the virtual environment in PowerShell:
# .venv\Scripts\Activate.ps1
```
You can view the interactive API documentation at `http://localhost:8000/api/docs`. 
For full endpoint payloads and Postman integration instructions, please see [API Documentation](api_documentation.md).

---

## 2. Frontend (Next.js)
The frontend is a React application built with Next.js App Router and TailwindCSS.

### Running the UI
```bash
cd frontend
# Install dependencies
npm install
# Start the development server on port 3000
npm run dev
```

Visit `http://localhost:3000` to access the main interface.
