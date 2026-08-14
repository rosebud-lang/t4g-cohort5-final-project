# StitchFlow API

## Project Overview
StitchFlow API is a backend application inspired by my mother's embroidery business. The business currently operates manually, making it difficult to track clients, orders, and payments. This project was built to demonstrate how backend technologies can be used to organize and improve small business operations through a structured RESTful API.

This project was developed as the final backend project for the Tech4Girls Cohort 5 Backend Development Program. It follows a layered architecture using SQLAlchemy models, Pydantic schemas, repositories, services, and FastAPI routes to keep the code modular, organized, and easy to maintain. 

## Features
The API currently supports full CRUD (Create, Read, Update, Delete) operations for:

### Clients
- Create a new client
- View all clients
- View a client by ID
- Update client information
- Delete a client
- Prevent duplicate email addresses using a **409 Conflict** response

### Orders
- Create an embroidery order
- View all orders
- View an order by ID
- Update an order
- Delete an order

### Payments
- Record a payment
- View all payments
- View a payment by ID
- Update payment information
- Delete a payment

The project also includes automatic Swagger documentation for testing all endpoints.


## System Workflow
The StitchFlow API manages the embroidery business using the following workflow:

Client Registration

↓

Order Creation

↓

Payment Recording

A client is registered before placing an embroidery order, and every payment is linked to an existing order. This relationship ensures that business records remain organized and consistent.


## Technologies Used
- Python 3
- FastAPI
- SQLAlchemy ORM
- MySQL
- Pydantic
- Uvicorn
- python-dotenv
- Git
- GitHub
- Swagger UI (OpenAPI)


## Project Structure
```text
t4g-cohort5-final-project
│
├── repositories/
│   ├── client_repository.py
│   ├── order_repository.py
│   └── payment_repository.py
│
├── services/
│   ├── client_services.py
│   ├── order_services.py
│   └── payment_services.py
│
├── routes/
│   ├── client_routes.py
│   ├── order_routes.py
│   └── payment_routes.py
│
├── database.py
├── main.py
├── models.py
├── schemas.py
├── .env
└── README.md
```

## API Endpoints
### Clients
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /clients | Create client |
| GET | /clients | Get all clients |
| GET | /clients/{client_id} | Get client by ID |
| PATCH | /clients/{client_id} | Update client |
| DELETE | /clients/{client_id} | Delete client |


### Orders
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /orders | Create order |
| GET | /orders | Get all orders |
| GET | /orders/{order_id} | Get order by ID |
| PATCH | /orders/{order_id} | Update order |
| DELETE | /orders/{order_id} | Delete order |


### Payments
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /payments | Create payment |
| GET | /payments | Get all payments |
| GET | /payments/{payment_id} | Get payment by ID |
| PATCH | /payments/{payment_id} | Update payment |
| DELETE | /payments/{payment_id} | Delete payment |


## Error Handling
The API returns meaningful HTTP status codes.
Examples include:

- **200 OK** – Request successful
- **201 Created** – Resource created successfully
- **404 Not Found** – Resource does not exist
- **409 Conflict** – Duplicate client email
- **422 Unprocessable Entity** – Invalid request data



## How to Run
### Clone the repository
```bash
git clone https://github.com/rosebud-lang/t4g-cohort5-final-project.git
```

### Move into the project
```bash
cd t4g-cohort5-final-project 
```

### Create a virtual environment
```bash
python -m venv .venv
```

### Activate the virtual environment
```bash
Windows
.venv\Scripts\activate
```

```bash
Linux/MacOs 
source .venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create a .env file
```env
DATABASE_URL=mysql+mysqlconnector://username:password@localhost/stitchflow_db
```


### Start the application
```bash
uvicorn main:app --reload
```

## API Documentation
### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```


## Future Improvements
Future versions of StitchFlow could include:
- User authentication and login
- Role-based access control
- File upload for embroidery designs
- Customer dashboard
- Invoice generation
- Email notifications
- Payment gateway integration
- Analytics and reporting
- Frontend web application


## Author
**Sedem Rosebud Awuah** Backend Developer

Final Backend Project
Tech4Girls Cohort 5 Backend Development Program
This project demonstrates how backend development concepts can be applied to solve real business problems through a structured and maintainable RESTful API.

## Acknowledgements
Special thanks to the Tech4Girls instructors and mentors for their guidance throughout the Backend Development Program.
