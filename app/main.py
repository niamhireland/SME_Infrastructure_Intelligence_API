from fastapi import FastAPI
from app.routes import recommend

app = FastAPI(title="SME Infrastructure Intelligence API")

app.include_router(recommend.router)

@app.get("/health")
def health():
    return {"status": "running"}