from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from models import Client
from repositories.client_repository import ClientRepository


class ClientService:
    """Handles business logic for clients."""

    def __init__(self, repository: ClientRepository):
        self.repository = repository


    def create_client(self, client_data):
        """Create a new client after checking business rules."""

        new_client = Client(
            name=client_data.name,
            phone=client_data.phone,
            email=client_data.email,
            organization_name=client_data.organization_name
        )

        try:
            return self.repository.create_client(new_client)

        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A client with this email already exists."
            )


    def get_all_clients(self):
        """Return all registered clients."""

        return self.repository.get_all_clients()


    def get_client_by_id(self, client_id):
        """Return one client or raise an error if not found."""

        client = self.repository.get_client_by_id(client_id)

        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found."
            )

        return client


    def update_client(self, client_id, client_data):
        """Update an existing client's information."""

        client = self.get_client_by_id(client_id)

        if client_data.name is not None:
            client.name = client_data.name

        if client_data.phone is not None:
            client.phone = client_data.phone

        if client_data.email is not None:
            client.email = client_data.email

        if client_data.organization_name is not None:
            client.organization_name = client_data.organization_name

        try:
            return self.repository.update_client(client)

        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A client with this email already exists."
            )


    def delete_client(self, client_id):
        """Delete a client if the client exists."""

        client = self.get_client_by_id(client_id)

        self.repository.delete_client(client)

        return {
            "message": "Client deleted successfully."
        }