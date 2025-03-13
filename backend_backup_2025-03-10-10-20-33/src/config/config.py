import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Server Configuration
BACKEND_HOST = os.getenv("BACKEND_HOST", "127.0.0.1")
BACKEND_PORT = int(os.getenv("BACKEND_PORT", 8000))
FRONTEND_HOST = os.getenv("FRONTEND_HOST", "127.0.0.1")
FRONTEND_PORT = int(os.getenv("FRONTEND_PORT", 3000))

# ✅ AI Processing Configuration
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
ENABLE_SUMMARIZATION = os.getenv("ENABLE_SUMMARIZATION", "true").lower() == "true"

# ✅ Security & Authentication
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# ✅ Logging & Debugging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"

# ✅ CORS Configuration
DEFAULT_ALLOWED_ORIGINS = "http://127.0.0.1:3000,http://localhost:3000"
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", DEFAULT_ALLOWED_ORIGINS).split(",")

# ✅ Fetch Configuration
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", 600))

# ✅ API Keys
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
MEDIASTACK_API_KEY = os.getenv("MEDIASTACK_API_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
