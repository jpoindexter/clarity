from fastapi import FastAPI
from backend.api.router import include_routers
include_routers(app)
include_routers(app)

# ✅ Create FastAPI App with a Global Prefix
app = FastAPI(root_path="/api")  # 👈 This ensures all routes are under /api/

# ✅ Register Routers
include_routers(app)

# ✅ Health Check
@app.get("/health")
def health_check():
    return {"status": "ok"}

include_routers(app)  # Ensure include_routers is properly called
