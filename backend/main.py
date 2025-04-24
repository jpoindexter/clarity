from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.endpoints import (
    summarize, 
    news,
    articles,
    analyze,
    fetch,
    search
)
from backend.agents.ingest_mesh import start_ingest_mesh
   
# ✅ Initialize FastAPI application
app = FastAPI(title="Clarity AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

# ✅ Include all API routes
app.include_router(summarize.router)
app.include_router(news.router)
app.include_router(articles.router)
app.include_router(analyze.router)
app.include_router(fetch.router)
app.include_router(search.router)
 
  
# ✅ Root route for testing
@app.get("/")
def root():
    return {"message": "Welcome to Clarity AI"} 


# ✅ Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# ✅ Ping route for uptime confirmation
@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.on_event("startup")
async def startup_event():
    start_ingest_mesh()