# 📡 Device Data API

Сервис для приёма и анализа телеметрических данных от устройств с возможностью получения агрегированной статистики по каждому устройству.

![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Dockerized-yes-blue?logo=docker)

---

## 🚀 Стек технологий

- 🐍 Python 3.11
- ⚡ FastAPI
- 🐘 PostgreSQL
- 🐳 Docker + Docker Compose
- 🧵 Async SQLAlchemy + asyncpg
- 📄 Pydantic

---

## 📦 Быстрый старт

> ⚠️ Убедитесь, что установлены Docker и Docker Compose

    ```bash
    # Клонировать репозиторий
    git clone https://github.com/IamGagik/device-data-api.git
    cd device-data-api

    #Запустить проект
    ```bash
    docker-compose up --build
    ```

После запуска сервис будет доступен по адресу:
👉 http://localhost:8000/docs — Swagger UI (интерактивная документация)

---

## 🧠 Функциональность

🔸 Добавление данных с устройствa
    ```bash
    POST /devices/{device_id}/data
    ```

Пример запроса:
    ```json
    {
    "x": 10.5,
    "y": 4.2,
    "z": 6.3
    }
    ```

Пример ответа:
    ```json
    {
    "status": "saved"
    }
    ```

🔸 Получение агрегированной статистики
    ```bash
    GET /devices/{device_id}/analysis
    ```

Пример ответа:
    ```json
    {
    "min": 21.0,
    "max": 33.4,
    "count": 5,
    "sum": 112.5,
    "median": 23.7
    }
    ```

⚙️ Настройка .env
Создай в корне проекта файл .env и добавь строку:
    ```bash
    DATABASE_URL=postgresql+asyncpg://user:password@db:5432/devices
    ```

---

## 🗂️ Структура проекта
    ```bash
    app/
    ├── api/          # Роуты FastAPI
    ├── db/           # Подключение к БД и модели
    ├── schemas/      # Pydantic-схемы (валидаторы)
    ├── services/     # Бизнес-логика (анализ)
    └── main.py       # Точка входа
    ```

---

## 👨‍💻 Автор
Разработано с душой ❤️
GitHub: @IamGagik

---