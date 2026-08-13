from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from uuid import uuid4
from database import Base


# Generate a unique ID for every new database record
def generate_uuid():
    """Generate a unique UUID."""
    return str(uuid4())


# =========================
# CLIENT MODEL
# =========================

class Client(Base):
    """Represents a client of the embroidery business."""

    __tablename__ = "clients"

    id = Column(
        String(50),
        primary_key=True,
        default=generate_uuid
    )

    name = Column(
        String(100),
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=True
    )

    organization_name = Column(
        String(150),
        nullable=True
    )

    # One client can place many orders
    orders = relationship(
        "Order",
        back_populates="client"
    )

    def __str__(self):
        return (
            f"Client ID: {self.id}, "
            f"Name: {self.name}, "
            f"Phone: {self.phone}, "
            f"Email: {self.email}, "
            f"Organization: {self.organization_name}"
        )


# =========================
# ORDER MODEL
# =========================

class Order(Base):
    """Represents an embroidery order placed by a client."""

    __tablename__ = "orders"

    id = Column(
        String(50),
        primary_key=True,
        default=generate_uuid
    )

    client_id = Column(
        String(50),
        ForeignKey("clients.id"),
        nullable=False
    )

    customer_type = Column(
        String(50),
        nullable=False
    )

    item_type = Column(
        String(50),
        nullable=False
    )

    design_description = Column(
        String(255),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    total_amount = Column(
        Float,
        nullable=False
    )

    due_date = Column(
        Date,
        nullable=True
    )

    status = Column(
        String(50),
        nullable=False,
        default="awaiting_deposit"
    )

    # Each order belongs to one client
    client = relationship(
        "Client",
        back_populates="orders"
    )

    # One order can have many payments
    payments = relationship(
        "Payment",
        back_populates="order"
    )

    def __str__(self):
        return (
            f"Order ID: {self.id}, "
            f"Client ID: {self.client_id}, "
            f"Item: {self.item_type}, "
            f"Quantity: {self.quantity}, "
            f"Total Amount: {self.total_amount}, "
            f"Due Date: {self.due_date}, "
            f"Status: {self.status}"
        )


# =========================
# PAYMENT MODEL
# =========================

class Payment(Base):
    """Represents a payment made towards an order."""

    __tablename__ = "payments"

    id = Column(
        String(50),
        primary_key=True,
        default=generate_uuid
    )

    order_id = Column(
        String(50),
        ForeignKey("orders.id"),
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    payment_type = Column(
        String(50),
        nullable=False
    )

    payment_method = Column(
        String(50),
        nullable=False
    )

    payment_date = Column(
        Date,
        nullable=False
    )

    # Each payment belongs to one order
    order = relationship(
        "Order",
        back_populates="payments"
    )

    def __str__(self):
        return (
            f"Payment ID: {self.id}, "
            f"Order ID: {self.order_id}, "
            f"Amount: {self.amount}, "
            f"Type: {self.payment_type}, "
            f"Method: {self.payment_method}, "
            f"Payment Date: {self.payment_date}"
        )