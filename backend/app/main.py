from fastapi import FastAPI
from app.routes.health import router as health_router
from app.database.db import run_query
from app.routes.track import router as track_router
from app.routes.profile import router as profile_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost:5173",  # React dev server
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health_router)
app.include_router(track_router)
app.include_router(profile_router)

@app.get("/test-db")
def test_db():
    result = run_query("SELECT * FROM users;")
    return {"db_test": result}