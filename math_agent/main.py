from fastapi import FastAPI
from router.math_router import router as math_router
from core.knowledge_base import initialize_kb
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_kb()
    yield
    print("🧠 Shutting down Math Routing Agent...")

app = FastAPI(title="Math Routing Agent", version="1.0", lifespan=lifespan)

app.include_router(math_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Math Routing Agent!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)