# Bluestock Backend 

## Overview
Bluestock Backend is a **Django REST API** that powers the Bluestock platform, managing IPO (Initial Public Offerings) data and interactions.

This backend:
- Provides a **REST API** for managing IPOs.
- Uses **PostgreSQL** as the database.
- Supports **Django REST Framework** for API management.
- Implements **CORS, filtering, authentication**, and **pagination**.

---

## Features
✅ **CRUD operations** for IPOs  
✅ **Django REST Framework (DRF)** integration  
✅ **Django Filters** for IPO search & filtering  
✅ **PostgreSQL Database Support**  
✅ **CORS Support for frontend integration**  
✅ **API Documentation using drf_spectacular**  

---

##  Project Setup
Follow these steps to set up the backend:

###  1. Clone the Repository
```sh
git clone https://github.com/your-repo/bluestock-backend.git
cd bluestock-backend
```

###  2. Create a Virtual Environment
```sh
python -m venv .venv
```
Activate it:
- **Windows**: `\.venv\Scripts\activate`
- **Mac/Linux**: `source .venv/bin/activate`

###  3. Install Dependencies
```sh
pip install -r requirements.txt
```

###  4. Set Up PostgreSQL Database
1. Open **pgAdmin** or **PSQL shell**.
2. Create the database manually:
```sql
CREATE DATABASE bluestock_db;
GRANT ALL PRIVILEGES ON DATABASE bluestock_db TO postgres;
```
3. Update `bluestock/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bluestock_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

###  5. Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

###  6. Create a Superuser
```sh
python manage.py createsuperuser
```

###  7. Start the Development Server
```sh
python manage.py runserver
```
Access the API at: **http://127.0.0.1:8000/**

---

##  API Endpoints

| Method | Endpoint | Description |
|--------|-------------|----------------|
| **GET** | `/ipo/companies/` | List all IPOs |
| **POST** | `/ipo/companies/` | Create a new IPO (Admin only) |
| **GET** | `/ipo/companies/{id}/` | Retrieve IPO details |
| **PUT** | `/ipo/companies/{id}/` | Update IPO (Admin only) |
| **DELETE** | `/ipo/companies/{id}/` | Delete IPO (Admin only) |

 **Filters & Search** are enabled for IPO queries. You can filter IPOs using parameters such as:
```sh
/ipo/companies/?symbol=AAPL
/ipo/companies/?open_date=2025-05-01
```

---

##  Deployment (Optional)
To deploy Bluestock Backend:
1. Set up a **PostgreSQL database** on a cloud provider.
2. Use **Gunicorn & Nginx** for production.
3. Run migrations and collect static files:
```sh
python manage.py collectstatic
```
4. Deploy to **Heroku, AWS, or DigitalOcean**.

---

##  Contributing
1. Fork the repository.
2. Create a feature branch.
3. Commit changes and push.
4. Create a Pull Request (PR).

---

##  License
This project is **MIT Licensed**.

---
