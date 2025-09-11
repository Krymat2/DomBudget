# 🏠 Home Budget App

A web application for managing personal and shared budgets, built with **Django**.  
It allows you to create budgets, expense/income categories, add transactions, and generate PDF reports.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Krymat2/DomBudget
cd DomBudget
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Database migrations and start the server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
The application will be available at: http://localhost:8000

---

## 🧪Tests
```bash
python manage.py test
```

---

## 📂Structure of the project

```bash
budzetApp/            # Main Django app
  models.py           # Model definitions (Budgets, Categories, Transactions, Users)
  views.py            # View logic
  forms.py            # Django forms
  urls.py             # App URL routing
  templates/          # HTML templates
  static/             # CSS/JS files

BudzetDomowy/         # Project settings
  settings.py         # Django settings
  urls.py             # Server routing, delegates management to the app
```

For a full structure of project, see [STRUCTURE.md](docs/STRUCTURE.md).

For a full list of models, see [MODELS.md](docs/MODELS.md).

For a full list of views, see [VIEWS.md](docs/VIEWS.md).

---

## ✨ Features

For a full list of features, see [FEATURES.md](docs/FEATURES.md).

---

##  ️️📝 User Guide

For a full user  guide, see [USER_GUIDE.md](docs/USER_GUIDE.md).

---

## Developers
Adam Balicki    
Adam Czuchra    
Krzysztof Pustół

---

## 📄 License

MIT License – free to use, modify, and distribute.