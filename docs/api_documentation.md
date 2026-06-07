# API Documentation

The FastAPI backend automatically generates interactive OpenAPI documentation using Swagger UI and ReDoc. This is the best way to test the API directly from your browser, acting similarly to Postman.

## Accessing the Live Interactive Documentation
- **Swagger UI**: [http://localhost:8000/api/docs](http://localhost:8000/api/docs) (Best for interactive testing)
- **ReDoc**: [http://localhost:8000/api/redoc](http://localhost:8000/api/redoc) (Best for reading)
- **Raw OpenAPI JSON**: [http://localhost:8000/api/openapi.json](http://localhost:8000/api/openapi.json) (Import this directly into Postman)

---

## Endpoint Details

### 1. Chat Completion Endpoint
**URL:** `/api/chat`
**Method:** `POST`
**Description:** Processes a user message through the LangGraph AI Workflow. It detects intent, routes to a department, creates a ticket if necessary, and returns the AI's final response.

**Request Payload (JSON):**
```json
{
  "message": "I can't login to my cloud deployment console.",
  "user_id": "user_12345",
  "conversation_id": "conv_9876"
}
```

**Success Response (JSON):**
```json
{
  "reply": "Thank you for contacting M.AI Tech Solutions. Your Technical issue has been routed to our Cloud Operations team. A support ticket has been created. Ticket ID: SUP-2026-A1B2. We will look into your login issue immediately.",
  "conversation_id": "conv_9876",
  "ticket_created": true,
  "ticket_id": "SUP-2026-A1B2"
}
```

---

### 2. Dashboard Metrics
**URL:** `/api/dashboard/metrics`
**Method:** `GET`
**Description:** Retrieves aggregated analytics data for the dashboard (Agent activity, department issues, tokens saved).

**Query Parameters:**
- `timeframe` (string, optional): `"week"` or `"month"`. Defaults to `"week"`.

**Success Response (JSON):**
```json
{
  "agent_activity": [
    {"name": "Mon", "resolved": 20, "escalated": 2},
    {"name": "Tue", "resolved": 25, "escalated": 5}
  ],
  "department_issues": [
    {"name": "Technical", "value": 85},
    {"name": "Sales", "value": 40}
  ],
  "new_clients": 12,
  "tokens_saved": 32000
}
```

---

### 3. Retrieve User Tickets
**URL:** `/api/tickets/{user_id}`
**Method:** `GET`
**Description:** Returns a list of open and historical tickets associated with a specific user.

**Path Parameters:**
- `user_id` (string, required): The ID of the user.

**Success Response (JSON):**
```json
[
  {
    "id": "SUP-2026-A1B2",
    "user_id": "user_12345",
    "department": "Cloud Operations",
    "priority": "Medium",
    "status": "Open",
    "subject": "Login Issue",
    "description": "User cannot login to the deployment console.",
    "created_at": "2026-06-07T14:00:00Z"
  }
]
```

---

## Postman Integration
To use these endpoints in **Postman**:
1. Open Postman.
2. Click **Import**.
3. Select "Link" and paste: `http://localhost:8000/api/openapi.json`
4. Postman will automatically generate a complete collection with all parameters, payloads, and authentication configurations ready to use!
