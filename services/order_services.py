from fastapi import HTTPException, status

from models import Order
from repositories.order_repository import OrderRepository
from repositories.client_repository import ClientRepository


class OrderService:
    """Handles business logic for orders."""

    def __init__(
        self,
        order_repository: OrderRepository,
        client_repository: ClientRepository
    ):
        self.order_repository = order_repository
        self.client_repository = client_repository


    def create_order(self, order_data):
        """Create an order after confirming that the client exists."""

        client = self.client_repository.get_client_by_id(
            order_data.client_id
        )

        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found."
            )

        new_order = Order(
            client_id=order_data.client_id,
            customer_type=order_data.customer_type,
            item_type=order_data.item_type,
            design_description=order_data.design_description,
            quantity=order_data.quantity,
            total_amount=order_data.total_amount,
            due_date=order_data.due_date,
            status=order_data.status
        )

        return self.order_repository.create_order(new_order)


    def get_all_orders(self):
        """Return all embroidery orders."""

        return self.order_repository.get_all_orders()


    def get_order_by_id(self, order_id):
        """Return one order or raise an error if not found."""

        order = self.order_repository.get_order_by_id(order_id)

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found."
            )

        return order


    def update_order(self, order_id, order_data):
        """Update selected order information."""

        order = self.get_order_by_id(order_id)

        if order_data.customer_type is not None:
            order.customer_type = order_data.customer_type

        if order_data.item_type is not None:
            order.item_type = order_data.item_type

        if order_data.design_description is not None:
            order.design_description = order_data.design_description

        if order_data.quantity is not None:
            order.quantity = order_data.quantity

        if order_data.total_amount is not None:
            order.total_amount = order_data.total_amount

        if order_data.due_date is not None:
            order.due_date = order_data.due_date

        if order_data.status is not None:
            order.status = order_data.status

        return self.order_repository.update_order(order)


    def delete_order(self, order_id):
        """Delete an order if it exists."""

        order = self.get_order_by_id(order_id)

        self.order_repository.delete_order(order)

        return {
            "message": "Order deleted successfully."
        }