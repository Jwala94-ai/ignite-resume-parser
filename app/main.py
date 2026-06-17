from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.parse import (
    router as parse_router
)

from app.api.routes.report import (
    router as report_router
)

app = FastAPI(
    title="Ignite Resume Parser"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Resume Parsing Routes
app.include_router(
    parse_router,
    prefix="/api",
    tags=["Resume Parser"]
)

# PDF Report Routes
app.include_router(
    report_router,
    prefix="/api",
    tags=["Reports"]
)

@app.get("/")
def home():
    return {
        "message": "Ignite Resume Parser Running"
    }