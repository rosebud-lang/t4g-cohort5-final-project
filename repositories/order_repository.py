from sqlalchemy.orm import Session

from models import Order


class OrderRepository:
    """Handles all database operations for orders."""

    def __init__(self, db: Session):
        self.db = db


    def create_order(self, order):
        """Save a new order to the database."""

        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)

        return order


    def get_all_orders(self):
        """Return all orders."""

        return self.db.query(Order).all()


    def get_order_by_id(self, order_id):
        """Find one order using its ID."""

        return (
            self.db
            .query(Order)
            .filter(Order.id == order_id)
            .first()
        )


    def update_order(self, order):
        """Commit updated order information."""

        self.db.commit()
        self.db.refresh(order)

        return order


    def delete_order(self, order):
        """Delete an order."""

        self.db.delete(order)
        self.db.commit()


