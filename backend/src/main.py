# ✅ backend/src/api/main.py
from fastapi import FastAPI

from backend.src.api.router import include_routers  # Ensure this exists and is correct

# ✅ Initialize FastAPI application
app = FastAPI(title="Clarity AI")

# ✅ Include all API routes
include_routers(app)


# ✅ Root route for testing
@app.get("/")
def root():
    return {"message": "Welcome to Clarity AI"}


# ✅ Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
