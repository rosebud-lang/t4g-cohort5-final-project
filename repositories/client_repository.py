from sqlalchemy.orm import Session
from models import Client

class ClientRepository:
    """Handles all database operations for clients."""

    def __init__(self, db: Session):
        self.db = db

from sqlalchemy.orm import Session
from models import Client


class ClientRepository:
    """Handles all database operations for clients."""

    def __init__(self, db: Session):
        self.db = db


    def create_client(self, client):
        """Save a new client to the database."""

        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)

        return client


    def get_all_clients(self):
        """Return all clients."""

        return self.db.query(Client).all()


    def get_client_by_id(self, client_id):
        """Find one client using its ID."""

        return (
            self.db
            .query(Client)
            .filter(Client.id == client_id)
            .first()
        )


    def update_client(self, client):
        """Commit updated client information."""

        self.db.commit()
        self.db.refresh(client)

        return client


    def delete_client(self, client):
        """Delete a client."""

        self.db.delete(client)
        self.db.commit()