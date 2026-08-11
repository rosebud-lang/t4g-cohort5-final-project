from database import Base, engine
from models import Client, Order, Payment


# Create all database tables
Base.metadata.create_all(bind=engine)


print("StitchFlow database tables created successfully.")

