from sqlalchemy.orm import Session

from models import Payment


class PaymentRepository:
    """Handles all database operations for payments."""

    def __init__(self, db: Session):
        self.db = db


    def create_payment(self, payment):
        """Save a new payment to the database."""

        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)

        return payment


    def get_all_payments(self):
        """Return all payments."""

        return self.db.query(Payment).all()


    def get_payment_by_id(self, payment_id):
        """Find one payment using its ID."""

        return (
            self.db
            .query(Payment)
            .filter(Payment.id == payment_id)
            .first()
        )


    def update_payment(self, payment):
        """Commit updated payment information."""

        self.db.commit()
        self.db.refresh(payment)

        return payment


    def delete_payment(self, payment):
        """Delete a payment."""

        self.db.delete(payment)
        self.db.commit()
