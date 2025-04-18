# TestCode (Next.js + FastAPI + Redis)

## Overview

This project is a solution for implementing:

- **Frontend**: Next.js
- **Backend**: FastAPI with **Domain-Driven Design (DDD)** concept
- **Redis**: As a caching layer for prompt responses

---

## Key Design Decisions

- Using **Domain-Driven Design (DDD)** on backend to ensure clear separation between business logic, infrastructure, and external interfaces.
- Caching AI prompt responses via **Redis** to improve response time and minimize redundant requests.
- **Next.js with React Context + localStorage** on frontend to persist chat history across sessions and refresh.


---

## Implemented Solution

### Backend (FastAPI + DDD)

The backend uses a **Domain-Driven Design (DDD)** architecture that separates domain logic, application, infrastructure, and interfaces in a structured way per bounded context.

#### Modular Structure

```
modules/
-- ai_prompt/
---- application/
------ dto/
------ services/
-------- prompt_service.py
---- domain/
------ entities/
-------- prompt.py
------ value_objects/
-------- prompt_type.py
------ repositories/
-------- prompt_repository.py
---- infrastructure/
------ external_clients/
-------- gemini_client.py
-------- llama_client.py
------ repositories/
-------- prompt_repository_impl.py
---- interfaces/
------ controllers/
-------- prompt_controller.py
------ api/
-------- prompt_router.py
```

#### Advantages:

- **Modular** and scalable
- **Decoupled**: Business logic is not dependent on FastAPI or storage
- **Testable**: Easy to isolate for unit testing
- **Flexible External Integration**: Simple to add new AI APIs

---

### Frontend (Next.js)

The frontend uses Next.js with several features:

- **Chat History**: Stored in **React Context + localStorage** to persist even after refresh or page navigation

---

## API Documentation

Accessible at http://localhost:8100/docs or through the provided openapi.json file

---

## Installation & Run Instructions

### 1️ Clone the Repository

```bash
git clone https://github.com/agustriad/coding-test-interopera.git
cd coding-test-interopera
```

### 2️ Folder Structure

```
/backend
/frontend
/docker-compose.yml
/README.md
```

### 3️ Run via Docker Compose

```bash
docker-compose up --build
```

- **frontend**: http://localhost:3000
- **backend (FastAPI)**: http://localhost:8100
- **redis**: default port 6379

### 4️ Environment Variables

#### Backend (.env)

```
ENV=development
PORT=8100
LOG_LEVEL=debug

#REDIS
REDIS_HOST=redis
REDIS_PORT=6379

#EXT CLIENT
GEMINI_URL=https://generativelanguage.googleapis.com/
GEMINI_APIKEY=__API__KEY__
GEMINI_MODEL=gemini-2.0-flash
```

#### Frontend (.env.local)

```
NEXT_PUBLIC_BACKEND_URL=http://localhost:8100
```

---

## Potential Improvements

- Implement **Event-Driven Architecture** for real-time integration
- Add **unit tests & integration tests**
- Apply **CQRS pattern** as the project scales
- Add **automatic multi-AI provider selection**
- Implement websocket transport for full-duplex communication

---

## Author

- Name: [Agus Triadji]
- Email: [agus.triadji@gmail.com]
- LinkedIn: [\[linkedin.com/in/agus-triadji-7b69942b\]](https://www.linkedin.com/in/agus-triadji-7b69942b/)

---
