BookMyShow Simplified Version
**Payment Features will be Added 

This project is a simplified version of the BookMyShow website built using Django. It includes features such as user registration, login, event management, ticket booking, and payment handling. The project uses Django REST Framework (DRF) for API development and SQLite as the database. The APIs can be tested using Postman or a web browser.

Features
User Authentication: Users can register and log in using APIs.
Event Management: Admins can add, update, and delete events.
Ticket Booking: Users can book tickets for events.
Payment Handling: Basic structure for payment gateway integration.
Django REST Framework: All features are accessible via REST APIs.
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.8+
Django 4.x
Django REST Framework
SQLite (default for Django, or you can configure another database)
Project Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/venketesh/bookmyshow-simplified.git
cd bookmyshow-simplified
2. Create a Virtual Environment and Activate It
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3. Install the Required Packages
bash
Copy code
pip install -r requirements.txt
4. Apply Migrations
bash
Copy code
python manage.py migrate
5. Create a Superuser (for Admin Access)
bash
Copy code
python manage.py createsuperuser
6. Run the Development Server
bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/admin to access the Django admin panel.

API Endpoints
User Authentication
Register: /users/register/

Method: POST
Payload:
json
Copy code
{
  "username": "testuser",
  "password": "testpassword"
}
Response: User details with a token (if authentication is implemented).
Login: /users/login/

Method: POST
Payload:
json
Copy code
{
  "username": "testuser",
  "password": "testpassword"
}
Response: Authentication token.
Event Management
Get All Events: /events/
Method: GET
Response: List of events.
Create Event (Admin Only): /events/create/
Method: POST
Payload:
json
Copy code
{
  "name": "Event Name",
  "date": "2024-10-10",
  "location": "Venue Name"
}
Ticket Booking
Book Ticket: /tickets/book/
Method: POST
Payload:
json
Copy code
{
  "event_id": 1,
  "number_of_tickets": 2
}
Response: Ticket booking confirmation.
Payment Handling
Make Payment: /payments/
Method: POST
Payload:
json
Copy code
{
  "booking_id": 1,
  "payment_method": "credit_card",
  "amount": 500.00
}
Response: Payment confirmation (this can be extended with real payment gateways).
Project Structure
graphql
Copy code
bookmyshow-simplified/
│
├── users/                  # User authentication app
│   ├── models.py           # User models
│   ├── views.py            # User views (Login, Register)
│   ├── urls.py             # URLs for login and register
│   └── serializers.py      # DRF serializers for user data
│
├── events/                 # Event management app
│   ├── models.py           # Event models
│   ├── views.py            # Event CRUD views
│   ├── urls.py             # URLs for event operations
│   └── serializers.py      # DRF serializers for event data
│
├── tickets/                # Ticket booking app
│   ├── models.py           # Ticket models
│   ├── views.py            # Ticket booking logic
│   ├── urls.py             # URLs for booking tickets
│   └── serializers.py      # DRF serializers for ticket data
│
├── payments/               # Payment handling app
│   ├── models.py           # Payment models
│   ├── views.py            # Payment processing logic
│   ├── urls.py             # URLs for payment processing
│   └── serializers.py      # DRF serializers for payment data
│
├── project_name/           # Main Django project folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project-level URL config
│   └── wsgi.py             # WSGI config for deployment
│
├── manage.py               # Django management script
└── README.md               # Project documentation
Testing
You can test the API endpoints using Postman or curl. For example:

bash
Copy code
curl -X POST http://127.0.0.1:8000/users/login/ \
  -d '{"username": "testuser", "password": "testpassword"}' \
  -H "Content-Type: application/json"
Admin Panel
The Django admin panel can be used to manage users, events, and tickets. Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
