# 📡 Device Data API

A service for receiving and analyzing telemetry data from devices, with the ability to retrieve aggregated statistics for each device.

![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Dockerized-yes-blue?logo=docker)

---

## 🚀 Tech Stack

- 🐍 Python 3.11  
- ⚡ FastAPI  
- 🐘 PostgreSQL  
- 🐳 Docker + Docker Compose  
- 🧵 Async SQLAlchemy + asyncpg  
- 📄 Pydantic  

---

## 📦 Quick Start

> ⚠️ Make sure you have Docker and Docker Compose installed

### 1. Clone the repository

```bash
git clone https://github.com/IamGagik/device-data-api.git
cd device-data-api
```

### 2. Run the project

```bash
docker-compose up --build
```

After starting, the service will be available at:  
👉 [http://localhost:8000/docs](http://localhost:8000/docs) — Swagger UI (interactive API documentation)

---

## 🧠 Features

### 🔹 Submit telemetry data from a device

```http
POST /devices/{device_id}/data
```

**Request example:**

```json
{
  "x": 10.5,
  "y": 4.2,
  "z": 6.3
}
```

**Response example:**

```json
{
  "status": "saved"
}
```

---

### 🔹 Get aggregated statistics for a device

```http
GET /devices/{device_id}/analysis
```

**Response example:**

```json
{
  "min": 21.0,
  "max": 33.4,
  "count": 5,
  "sum": 112.5,
  "median": 23.7
}
```

---

## ⚙️ .env Configuration

Create a `.env` file in the root of the project and add:

```env
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/devices
```

---

## 🗂️ Project Structure

```text
app/
├── api/          # FastAPI routes
├── db/           # DB connection and models
├── schemas/      # Pydantic models (validation)
├── services/     # Business logic (data analysis)
└── main.py       # Entry point
```

---

## 👨‍💻 Author

Made with ❤️ by  
**GitHub:** [@IamGagik](https://github.com/IamGagik)
