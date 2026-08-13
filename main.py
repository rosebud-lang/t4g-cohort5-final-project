from fastapi import FastAPI

from database import Base, engine
from routes.client_routes import router as client_router


# Create all database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="StitchFlow API",
    description="Backend API for managing embroidery clients, orders, and payments."
)


@app.get("/")
def home():
    """Home route."""

    return {
        "message": "Welcome to StitchFlow API"
    }


app.include_router(client_router)