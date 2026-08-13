from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read database connection string
connection_str = os.getenv("DATABASE_URL")

# Create database engine
engine = create_engine(
    connection_str,
    pool_pre_ping=True
)

# Configure the session
SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Create the base class
Base = declarative_base()