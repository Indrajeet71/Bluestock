# IPO Tracking System - Backend Documentation

## Project Overview
This is the backend service for the IPO Tracking System, built using Django Rest Framework (DRF) and PostgreSQL. It tracks, stores, and serves real-time IPO data fetched from the NSE API, enabling seamless data management and retrieval through a well-structured REST API.

## Tech Stack
| Component       | Technology               |
|----------------|--------------------|
| Backend Framework | Django Rest Framework (DRF) |
| Database        | PostgreSQL |
| Programming Language | Python |
| API Integration | NSE API |
| Task Scheduler  | APScheduler (Celery optional for production) |
| Deployment      | Localhost (can be Dockerized for production) |

## Folder Structure
```
bluestock/
├── ipo/                       # IPO App (Main App)
│   ├── migrations/            # DB Migrations
│   ├── serializers.py         # DRF Serializers
│   ├── urls.py                 # App-level URLs
│   ├── views.py                 # Core Business Logic
│   ├── models.py                # Database Models
│
├── bluestock/                   # Project-level Config
│   ├── settings.py              # Main Config File
│   ├── urls.py                   # Global URLs (includes IPO URLs)
│   ├── wsgi.py                   # WSGI Entry Point
│
├── manage.py                    # Django Command Utility
├── requirements.txt             # Python Packages
├── README.md                    # Project Documentation
```

## Database Schema - IPOCompany Model
| Field                  | Type       | Description |
|------------------|----------|--------------------|
| name                    | CharField  | Name of the company |
| symbol                  | CharField  | Company symbol (NSE) |
| issue_price            | DecimalField | IPO price per share |
| lot_size               | IntegerField | Minimum lot size |
| open_date            | DateField | IPO opening date |
| close_date            | DateField | IPO closing date |
| created_at              | DateTimeField | Record creation timestamp |
| updated_at             | DateTimeField | Last update timestamp |

## Key API Endpoints
| Method | Endpoint                | Description |
|------|-----------------|----------------|
| GET | /ipo/companies/ | List all IPOs (pagination, filtering supported) |
| POST | /ipo/companies/ | Add new IPO (admin only) |
| GET | /ipo/companies/{id}/ | Fetch single IPO details |
| PUT | /ipo/companies/{id}/ | Update IPO details (admin only) |
| DELETE | /ipo/companies/{id}/ | Delete IPO record (admin only) |

## Data Fetching Flow (NSE Integration)
1. Scheduled job (APScheduler) triggers every 24 hours.
2. It calls NSE API and fetches the latest IPO data.
3. New records are added, existing records are updated.
4. Data sanitization and validation are applied.
5. Database is updated for accurate and up-to-date information.

## Error Handling & Validation
- Each API call is validated using DRF serializers.
- Returns appropriate HTTP status codes (400, 404, 500) on errors.
- External API failures are logged with retry mechanisms.
- Data inconsistencies (missing fields, wrong formats) are auto-flagged and skipped.

## Performance Optimizations
- Database queries optimized using proper indexing where needed.
- Large payloads handled via pagination to ensure smooth response times.
- Bulk inserts instead of single-row inserts to reduce database overhead.

## Setup Instructions
1. Clone the Repository
```
git clone https://github.com/ishaan-vashist/ipo-tracking-backend.git
cd ipo-tracking-backend
```
2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Setup PostgreSQL Connection in `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
5. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
6. Run Development Server
```
python manage.py runserver
```
7. Access APIs
- List IPOs: [http://localhost:8000/ipo/companies/](http://localhost:8000/ipo/companies/)
- Admin Dashboard: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Recommended Tools
- Postman: API Testing
- pgAdmin: PostgreSQL Management
- GitHub: Version Control
- Celery/Redis: For production-level scheduled jobs

## Contributors
- [Ishaan Vashist](https://github.com/ishaan-vashist)

