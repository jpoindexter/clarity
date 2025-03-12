from fastapi import FastAPI
from backend.api.router import include_routers  # ✅ Ensure correct import

app = FastAPI()  # ✅ Ensure app is defined before calling include_routers

include_routers(app)  # ✅ Register all routers after app is defined


@app.get("/")
def root():
    return {"message": "Clarity API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}