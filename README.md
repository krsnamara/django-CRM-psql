# CRM Django Project

This Django project is a Customer Relationship Management (CRM) system. It provides a dashboard with information about total orders, orders delivered, and orders pending. Additionally, it allows users to manage customers and orders.
<br>
It is built from a tutorial by

[Dennis Ivy](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)

Deployment on Render using this
[Dennis Ivy](https://www.youtube.com/watch?v=wczWm8j4v9w)

## Getting Started

### Prerequisites

Before running the project, ensure you have the following installed:

- Python (3.8 or higher)
- Django (4.1.5)
- PostgreSQL

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables by creating a .env file in the project root. Include the following:

   ```bash
   SECRET_KEY=your_secret_key
   NAME=your_database_name
   USER=your_database_user
   PASSWORD=your_database_password
   HOST=your_database_host
   PORT=your_database_port
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

### To Run the Server

Run the development server:
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to access the CRM dashboard.

### Project Structure

crm: Django project settings and configuration.
accounts: Django app handling customer and order management.
static: Static files (CSS, JavaScript, Images).
templates: HTML templates used in the project.
Usage
Dashboard
The dashboard displays key information about total orders, orders delivered, and orders pending.

Customers
Manage customers, view details, and create new customers.

Orders
Create, update, and delete orders. The last 5 orders are displayed with product details, order date, and status.

Admin
Access the Django admin interface by visiting http://127.0.0.1:8000/admin. Use the superuser credentials created during migration to log in.

Technologies Used
Django
PostgreSQL
Bootstrap (4.3.1)
