from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import SessionFactory
from repositories.payment_repository import PaymentRepository
from repositories.order_repository import OrderRepository
from services.payment_services import PaymentService
from schemas import PaymentCreate, PaymentUpdate, PaymentResponse


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
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
    response_model=PaymentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_payment(
    payment_data: PaymentCreate,
    db: Session = Depends(get_db)
):
    """Record a new payment."""

    payment_repository = PaymentRepository(db)
    order_repository = OrderRepository(db)

    service = PaymentService(
        payment_repository,
        order_repository
    )

    return service.create_payment(payment_data)


@router.get(
    "",
    response_model=list[PaymentResponse],
    status_code=status.HTTP_200_OK
)
def get_all_payments(
    db: Session = Depends(get_db)
):
    """Return all recorded payments."""

    payment_repository = PaymentRepository(db)
    order_repository = OrderRepository(db)

    service = PaymentService(
        payment_repository,
        order_repository
    )

    return service.get_all_payments()


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse,
    status_code=status.HTTP_200_OK
)
def get_payment_by_id(
    payment_id: str,
    db: Session = Depends(get_db)
):
    """Return one payment by ID."""

    payment_repository = PaymentRepository(db)
    order_repository = OrderRepository(db)

    service = PaymentService(
        payment_repository,
        order_repository
    )

    return service.get_payment_by_id(payment_id)


@router.patch(
    "/{payment_id}",
    response_model=PaymentResponse,
    status_code=status.HTTP_200_OK
)
def update_payment(
    payment_id: str,
    payment_data: PaymentUpdate,
    db: Session = Depends(get_db)
):
    """Update selected payment information."""

    payment_repository = PaymentRepository(db)
    order_repository = OrderRepository(db)

    service = PaymentService(
        payment_repository,
        order_repository
    )

    return service.update_payment(
        payment_id,
        payment_data
    )


@router.delete(
    "/{payment_id}",
    status_code=status.HTTP_200_OK
)
def delete_payment(
    payment_id: str,
    db: Session = Depends(get_db)
):
    """Delete a payment."""

    payment_repository = PaymentRepository(db)
    order_repository = OrderRepository(db)

    service = PaymentService(
        payment_repository,
        order_repository
    )

    return service.delete_payment(payment_id) 
