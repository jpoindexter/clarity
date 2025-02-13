# Clarity - AI-Powered News Discovery Platform

## 📌 Project Overview

Clarity is an AI-powered news aggregation and discovery platform that provides users with unbiased, real-time insights from multiple sources. Built with **FastAPI** and **PostgreSQL**, it enables intelligent news filtering, search, and AI-powered summarization.

## 🚀 Features

- **AI-enhanced news aggregation** from diverse sources.
- **Searchable news feed** powered by FastAPI.
- **Automatic AI-generated summaries** for quick insights.
- **Real-time updates and filtering options**.
- **Responsive UI built with Next.js**.

## 📂 Project Structure

```bash
backend/
│── src/
│   ├── api/              # FastAPI endpoints
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── database/         # Database connection
│   ├── crud/             # CRUD operations
│   ├── utils/            # Helper functions
│── alembic/              # Database migrations
│── tests/                # Unit tests
frontend/
│── components/           # UI components
│── pages/                # Next.js pages
│── services/             # API calls from frontend
│── styles/               # Global styles
```

## 🛠️ Tech Stack

### **Backend**

- **Python** (FastAPI)
- **PostgreSQL**
- **SQLAlchemy**
- **Alembic** (Database migrations)
- **Uvicorn** (ASGI server)

### **Frontend**

- **Next.js** (React framework)
- **TailwindCSS** (Styling)
- **TypeScript** (Strict typing)

## 🏗️ Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/clarity.git
cd clarity
```

### **2️⃣ Backend Setup**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**

Create a `.env` file in the `backend` directory:

```ini
DATABASE_URL=postgresql://user:password@localhost:5432/clarity
SECRET_KEY=your_secret_key_here
DEBUG=True
```

### **4️⃣ Apply Database Migrations**

```bash
alembic upgrade head
```

### **5️⃣ Run the Backend Server**

```bash
uvicorn src.api.main:app --host 127.0.0.1 --port 8000 --reload
```

### **6️⃣ Frontend Setup**

```bash
cd frontend
npm install
npm run dev
```

## 🔗 API Documentation

FastAPI provides automatic API documentation:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🛠️ Running Tests

```bash
pytest
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Added new feature'`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request 🚀

## 📜 License

This project is licensed under the **Business Source License (BSL) 1.1**.

### **Business Source License (BSL) 1.1**

**Change Date:** 2027-02-13 _(3 years from now, it may transition to Apache 2.0 or another license at Clarity Technologies’ discretion.)_

**Use Restrictions:**

- **Commercial use requires a paid license** from Clarity Technologies.
- **No competing AI news aggregation platforms** may use this software **without explicit permission**.
- **Personal, non-commercial use is allowed**.

For commercial licensing and permission requests, contact: **legal@claritytech.com**

Copyright © 2025 Clarity Technologies. All rights reserved.
