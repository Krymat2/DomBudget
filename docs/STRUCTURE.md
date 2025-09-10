# 📂 Project Structure – Home Budget App

This document explains the folder and file structure of the **Home Budget App** Django project.

---

## Root Directory

```bash
DomBudget/
│
├── budzetApp/ # Main Django application
│ ├── models.py # Database models (Budgets, Categories, Transactions, Users)
│ ├── views.py # View logic for handling requests
│ ├── forms.py # Django forms
│ ├── urls.py # URL routing for this app
│ ├── admin.py # Django admin configurations
│ ├── tests.py # Automated tests for this app
│ ├── templates/ # HTML templates for the app
│ │ └── budzetApp/ # Template files organized per app
│ └── static/ # Static files (CSS, JS, images)
│
├── BudzetDomowy/ # Project configuration folder
│ ├── settings.py # Django settings
│ ├── urls.py # Project-level URL routing
│ ├── wsgi.py # WSGI configuration
│ └── asgi.py # ASGI configuration
│
├── docs/ 
│ ├── README.md # Project overview
│ ├── STRUCTURE.md # Project structure
│ ├── MODELS.md # Project models
│ ├── USER_GUIDE.md # Project user guide
│ └── FEATURES.md # List of features
│
├── manage.py # Django management script
├── db.sqlite3 # Example database file
└── requirements.txt # Python dependencies
```

---

## 📄 Folder Details

### `budzetApp/`
- **models.py** – defines database models: `Budżety`, `Kategorie`, `Transakcje`, `Użytkownicy`  
- **views.py** – contains the logic for handling HTTP requests and rendering templates  
- **forms.py** – Django forms for input validation  
- **urls.py** – routes URLs to views  
- **admin.py** – configurations for Django admin interface  
- **templates/** – HTML files used by the app  
- **static/** – CSS, JavaScript, and images  

### `BudzetDomowy/`
- **settings.py** – Django project settings (databases, installed apps, middleware, etc.)  
- **urls.py** – project-level URL configuration, delegates to apps  
- **wsgi.py / asgi.py** – web server interfaces  

### `docs/`
- **README.md** – Project overview  
- **STRUCTURE.md** – Project structure  
- **MODELS.md** – Documentation of project models  
- **USER_GUIDE.md** – End-user guide  
- **FEATURES.md** – List of features


### Root files
- **manage.py** – CLI tool for running Django commands  
- **requirements.txt** – project dependencies  
- **README.md** – overview of the project  
- **INSTALLATION.md** – installation and setup guide  
- **FEATURES.md** – list of application features  
- **docs/** – additional documentation (optional)

---

This structure helps developers quickly understand the layout and purpose of each folder and file in the project.
