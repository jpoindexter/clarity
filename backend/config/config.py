import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Server Configuration
BACKEND_HOST = os.getenv("BACKEND_HOST", "127.0.0.1")
<<<<<<< HEAD
BACKEND_PORT = int(os.getenv("BACKEND_PORT", 8000))
FRONTEND_HOST = os.getenv("FRONTEND_HOST", "127.0.0.1")
FRONTEND_PORT = int(os.getenv("FRONTEND_PORT", 3000))
=======
BACKEND_PORT = int(os.getenv("BACKEND_PORT", "8000").strip())
FRONTEND_HOST = os.getenv("FRONTEND_HOST", "127.0.0.1")
FRONTEND_PORT = int(os.getenv("FRONTEND_PORT", "3000").strip())
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917

# ✅ AI Processing Configuration
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
ENABLE_SUMMARIZATION = os.getenv("ENABLE_SUMMARIZATION", "true").lower() == "true"

# ✅ Security & Authentication
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
<<<<<<< HEAD
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
=======
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
    .strip()
    .split('#')[0]
    .strip()
)
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917

# ✅ Logging & Debugging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"

# ✅ CORS Configuration
DEFAULT_ALLOWED_ORIGINS = "http://127.0.0.1:3000,http://localhost:3000"
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", DEFAULT_ALLOWED_ORIGINS).split(",")

# ✅ Fetch Configuration
<<<<<<< HEAD
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", 600))
=======
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", "600").split("#")[0].strip())
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917

# ✅ API Keys
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")
MEDIASTACK_API_KEY = os.getenv("MEDIASTACK_API_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
