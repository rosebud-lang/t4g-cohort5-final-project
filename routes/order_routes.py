from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import SessionFactory
from repositories.order_repository import OrderRepository
from repositories.client_repository import ClientRepository
from services.order_services import OrderService
from schemas import OrderCreate, OrderUpdate, OrderResponse


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
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
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED
)
def create_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db)
):
    """Create a new embroidery order."""

    order_repository = OrderRepository(db)
    client_repository = ClientRepository(db)

    service = OrderService(
        order_repository,
        client_repository
    )

    return service.create_order(order_data)


@router.get(
    "",
    response_model=list[OrderResponse],
    status_code=status.HTTP_200_OK
)
def get_all_orders(
    db: Session = Depends(get_db)
):
    """Return all embroidery orders."""

    order_repository = OrderRepository(db)
    client_repository = ClientRepository(db)

    service = OrderService(
        order_repository,
        client_repository
    )

    return service.get_all_orders()


@router.get(
    "/{order_id}",
    response_model=OrderResponse,
    status_code=status.HTTP_200_OK
)
def get_order_by_id(
    order_id: str,
    db: Session = Depends(get_db)
):
    """Return one order by ID."""

    order_repository = OrderRepository(db)
    client_repository = ClientRepository(db)

    service = OrderService(
        order_repository,
        client_repository
    )

    return service.get_order_by_id(order_id)


@router.patch(
    "/{order_id}",
    response_model=OrderResponse,
    status_code=status.HTTP_200_OK
)
def update_order(
    order_id: str,
    order_data: OrderUpdate,
    db: Session = Depends(get_db)
):
    """Update selected order information."""

    order_repository = OrderRepository(db)
    client_repository = ClientRepository(db)

    service = OrderService(
        order_repository,
        client_repository
    )

    return service.update_order(
        order_id,
        order_data
    )


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_200_OK
)
def delete_order(
    order_id: str,
    db: Session = Depends(get_db)
):
    """Delete an order."""

    order_repository = OrderRepository(db)
    client_repository = ClientRepository(db)

    service = OrderService(
        order_repository,
        client_repository
    )

    return service.delete_order(order_id)

