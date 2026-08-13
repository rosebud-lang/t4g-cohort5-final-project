from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import SessionFactory
from repositories.client_repository import ClientRepository
from services.client_services import ClientService
from schemas import ClientCreate, ClientUpdate, ClientResponse


router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)


def get_db():
    """Provide a database session for each request."""
    db = SessionFactory() 
    
    try:
        yield db

    finally:
        db.close()


@router.post(
    "",
    response_model=ClientResponse,
    status_code=status.HTTP_201_CREATED
)
def create_client(
    client_data: ClientCreate,
    db: Session = Depends(get_db)
): 
    """Create a new client."""

    repository = ClientRepository(db)
    service = ClientService(repository)

    return service.create_client(client_data)


@router.get(
    "",
    response_model=list[ClientResponse],
    status_code=status.HTTP_200_OK
)
def get_all_clients(
    db: Session = Depends(get_db)

):
    """Return all registered clients."""

    repository = ClientRepository(db)
    service = ClientService(repository)

    return service.get_all_clients()


@router.get(
    "/{client_id}",
    response_model=ClientResponse,
    status_code=status.HTTP_200_OK
)
def get_client_by_id(
    client_id: str,
    db: Session = Depends(get_db)
):
    """Return one client by ID."""

    repository = ClientRepository(db)
    service = ClientService(repository)

    return service.get_client_by_id(client_id)


@router.patch(
    "/{client_id}",
    response_model=ClientResponse,
    status_code=status.HTTP_200_OK
)
def update_client(
    client_id: str,
    client_data: ClientUpdate,
    db: Session = Depends(get_db)
):
    """Update selected client information."""

    repository = ClientRepository(db)
    service = ClientService(repository)

    return service.update_client(
        client_id,
        client_data
    )


@router.delete(
    "/{client_id}",
    status_code=status.HTTP_200_OK
)

def delete_client(
    client_id: str,
    db: Session = Depends(get_db)
):
    """Delete a client."""

    repository = ClientRepository(db)
    service = ClientService(repository)

    return service.delete_client(client_id)