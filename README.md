# Good Life

A Django-based web application.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- PostgreSQL

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd good_life
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL:
```bash
# Create PostgreSQL database
createdb good_life

# Or using psql:
psql -U postgres
CREATE DATABASE good_life;
```

5. Run database migrations:
```bash
python manage.py migrate
```

## Running the Application

1. Make sure your virtual environment is activated:
```bash
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows
```

2. Start the development server:
```bash
python manage.py runserver
```

3. Open your web browser and visit:
```
http://127.0.0.1:8000/
```

## API Endpoints

The following API endpoints are available:

- `GET /api/habits/` - List all habits
- `POST /api/habits/` - Create a new habit
- `GET /api/habits/{id}/` - Retrieve a specific habit
- `PUT /api/habits/{id}/` - Update a specific habit
- `DELETE /api/habits/{id}/` - Delete a specific habit

Example POST/PUT request body:
```json
{
    "title": "Morning Exercise",
    "days_of_week": ["MON", "WED", "FRI"]
}
```

## Development

The project structure is organized as follows:
```
good_life/
├── core/                 # Main application
│   ├── views.py         # View definitions
│   ├── models.py        # Database models
│   ├── serializers.py   # API serializers
│   └── urls.py          # URL routing
├── good_life/           # Project settings
│   ├── settings.py      # Project configuration
│   └── urls.py          # Main URL routing
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── venv/               # Virtual environment
```

## Stopping the Server

To stop the development server, press `Ctrl+C` in the terminal where the server is running. 