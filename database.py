from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read the database connection string
connection_str = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(
    connection_str,
    pool_pre_ping=True
)

# Create a session factory
SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False, 
    autocommit=False
)

# Base class for all models
Base = declarative_base()

