# ✅ backend/src/api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from starlette.requests import Request

from backend.src.api.router import include_routers  # Ensure this exists and is correct

# ✅ Initialize FastAPI application
app = FastAPI(title="Clarity AI")

# ✅ Enable Cross-Origin Resource Sharing (CORS) if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Adjust this in production (e.g., ["https://yourfrontend.com"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Configure Rate Limiting (Prevents API abuse)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

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


# ✅ API Rate-Limited Endpoint Example

@app.get("/api/v1/articles", tags=["articles"])
@limiter.limit("1000 per minute")  # Adjust rate as needed
async def get_articles(request: Request):
    return {"message": "This is a rate-limited example for fetching articles."}


# ✅ Performance Logging Middleware
@app.middleware("http")
async def log_request_time(request: Request, call_next):
    from time import time
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
