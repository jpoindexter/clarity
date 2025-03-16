import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set")

# ✅ Server Configuration
BACKEND_HOST = os.getenv("BACKEND_HOST", "127.0.0.1")
BACKEND_PORT = (
    int(os.getenv("BACKEND_PORT", "8000").strip())
    if os.getenv("BACKEND_PORT")
    else 8000
)
FRONTEND_HOST = os.getenv("FRONTEND_HOST", "127.0.0.1")
FRONTEND_PORT = (
    int(os.getenv("FRONTEND_PORT", "3000").strip())
    if os.getenv("FRONTEND_PORT")
    else 3000
)

# ✅ AI Processing Configuration
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
ENABLE_SUMMARIZATION = os.getenv("ENABLE_SUMMARIZATION", "true").lower() == "true"

# ✅ Security & Authentication
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
if not SECRET_KEY and os.getenv("ENV") == "production":
    raise ValueError("SECRET_KEY must be set in production")

ACCESS_TOKEN_EXPIRE_MINUTES = (
    int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60").strip())
    if os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    else 60
)
DEFAULT_ALLOWED_ORIGINS = "http://127.0.0.1:3000,http://localhost:3000"
ALLOWED_ORIGINS = list(
    filter(None, os.getenv("ALLOWED_ORIGINS", DEFAULT_ALLOWED_ORIGINS).split(","))
)

# ✅ Fetch Configuration
FETCH_INTERVAL = (
    int(os.getenv("FETCH_INTERVAL", "600").strip())
    if os.getenv("FETCH_INTERVAL")
    else 600
)

# ✅ Additional Configurations
# Add any additional configuration variables below this line.

if os.getenv("DEBUG", "false").lower() == "true":
    print(
        f"Loaded Config: DATABASE_URL={DATABASE_URL}, "
        f"BACKEND_HOST={BACKEND_HOST}, BACKEND_PORT={BACKEND_PORT}"
    )
