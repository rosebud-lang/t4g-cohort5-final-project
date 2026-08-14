from fastapi import FastAPI

from database import Base, engine
from routes.client_routes import router as client_router
from routes.order_routes import router as order_router
from routes.payment_routes import router as payment_router 

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
app.include_router(order_router)
app.include_router(payment_router) 


