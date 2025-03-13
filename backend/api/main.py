import logging
import os
from logging.config import dictConfig
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from starlette.requests import Request

from backend.api.router import include_routers

# ✅ Ensure log directory exists
LOG_DIR = "backend/logs"
LOG_FILE = os.path.join(LOG_DIR, "clarity-api.log")

os.makedirs(LOG_DIR, exist_ok=True)  # ✅ Create logs directory if missing

# ✅ Logging Configuration
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "default",
            "mode": "a",  # ✅ Appends instead of overwriting
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["file", "console"], "level": "INFO"},
        "fastapi": {"handlers": ["file", "console"], "level": "INFO"},
    },
}
dictConfig(logging_config)
logger = logging.getLogger("fastapi")

# ✅ Initialize FastAPI application
app = FastAPI(title="Clarity AI")

# ✅ Enable Cross-Origin Resource Sharing (CORS) if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production (e.g., ["https://yourfrontend.com"])
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

# ✅ Performance Logging Middleware


@app.middleware("http")
async def log_requests(request: Request, call_next):
    from time import time
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time

    logger.info(
        f"{request.method} {request.url} - "
        f"Status: {response.status_code} - "
        f"Time: {process_time:.4f}s"
    )
    response.headers["X-Process-Time"] = str(process_time)
    return response
