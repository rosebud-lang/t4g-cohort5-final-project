from datetime import date
from pydantic import BaseModel, Field
from typing import Optional


# ==========================
# CLIENT SCHEMAS
# ==========================

class ClientCreate(BaseModel):
    """Schema for creating a new client."""

    name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=10, max_length=20)
    email: Optional[str] = None
    organization_name: Optional[str] = None


class ClientResponse(ClientCreate):
    """Schema returned after creating or retrieving a client."""

    id: str

    class Config:
        from_attributes = True

class ClientUpdate(BaseModel):
    """Schema for updating client information."""

    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    organization_name: Optional[str] = None 


# ==========================
# ORDER SCHEMAS
# ==========================

class OrderCreate(BaseModel):
    """Schema for creating a new embroidery order."""

    client_id: str
    customer_type: str
    item_type: str
    design_description: str
    quantity: int = Field(..., gt=0)
    total_amount: float = Field(..., gt=0)
    due_date: Optional[date] = None
    status: str = "awaiting_deposit"


class OrderUpdate(BaseModel):
    """Schema for updating selected order information."""

    customer_type: Optional[str] = None
    item_type: Optional[str] = None
    design_description: Optional[str] = None
    quantity: Optional[int] = Field(None, gt=0)
    total_amount: Optional[float] = Field(None, gt=0)
    due_date: Optional[date] = None
    status: Optional[str] = None


class OrderResponse(OrderCreate):
    """Schema returned after creating or retrieving an order."""

    id: str

    class Config:
        from_attributes = True


# ==========================
# PAYMENT SCHEMAS
# ==========================

class PaymentCreate(BaseModel):
    """Schema for recording a payment."""

    order_id: str
    amount: float = Field(..., gt=0)
    payment_type: str
    payment_method: str
    payment_date: date

class PaymentUpdate(BaseModel):
    """Schema for updating selected payment information."""

    amount: Optional[float] = Field(None, gt=0)
    payment_type: Optional[str] = None
    payment_method: Optional[str] = None
    payment_date: Optional[date] = None 


class PaymentResponse(PaymentCreate):
    """Schema returned after recording a payment."""

    id: str

    class Config:
        from_attributes = True

