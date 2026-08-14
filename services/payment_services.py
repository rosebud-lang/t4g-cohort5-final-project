from fastapi import HTTPException, status

from models import Payment
from repositories.payment_repository import PaymentRepository
from repositories.order_repository import OrderRepository


class PaymentService:
    """Handles business logic for payments."""

    def __init__(
        self,
        payment_repository: PaymentRepository,
        order_repository: OrderRepository
    ):
        self.payment_repository = payment_repository
        self.order_repository = order_repository


    def create_payment(self, payment_data):
        """Create a payment after confirming that the order exists."""

        order = self.order_repository.get_order_by_id(
            payment_data.order_id
        )

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found."
            )

        new_payment = Payment(
            order_id=payment_data.order_id,
            amount=payment_data.amount,
            payment_type=payment_data.payment_type,
            payment_method=payment_data.payment_method,
            payment_date=payment_data.payment_date
        )

        return self.payment_repository.create_payment(new_payment)


    def get_all_payments(self):
        """Return all recorded payments."""

        return self.payment_repository.get_all_payments()


    def get_payment_by_id(self, payment_id):
        """Return one payment or raise an error if not found."""

        payment = self.payment_repository.get_payment_by_id(
            payment_id
        )

        if not payment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found."
            )

        return payment


    def update_payment(self, payment_id, payment_data):
        """Update selected payment information."""

        payment = self.get_payment_by_id(payment_id)

        if payment_data.amount is not None:
            payment.amount = payment_data.amount

        if payment_data.payment_type is not None:
            payment.payment_type = payment_data.payment_type

        if payment_data.payment_method is not None:
            payment.payment_method = payment_data.payment_method

        if payment_data.payment_date is not None:
            payment.payment_date = payment_data.payment_date

        return self.payment_repository.update_payment(payment)


    def delete_payment(self, payment_id):
        """Delete a payment if it exists."""

        payment = self.get_payment_by_id(payment_id)

        self.payment_repository.delete_payment(payment)

        return {
            "message": "Payment deleted successfully."
        }

