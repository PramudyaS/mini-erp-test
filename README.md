# Mini ERP - Django Project

A lightweight ERP system built with **Python Django** and **PostgreSQL**.  

---

## 🚀 Getting Started

### 1. Create & Activate Virtual Environment
```
python3 -m venv myenv
source myenv/bin/activate
```

### 2. Install Dependencies
```
pip install django django-environ
pip install psycopg2-binary
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

---

## 🗄️ Database Setup

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## ▶️ Running the Server

```
python manage.py runserver
```

---

## 🗂️ Database Design

![Database Design](mini-erp.jpg)

---

## ⚡ Makefile Shortcuts

Create a `Makefile` in the project root:

```
ENV=myenv

setup:
    python3 -m venv $(ENV)
    source $(ENV)/bin/activate && pip install -r requirements.txt

migrate:
    source $(ENV)/bin/activate && python manage.py makemigrations && python manage.py migrate

superuser:
    source $(ENV)/bin/activate && python manage.py createsuperuser

run:
    source $(ENV)/bin/activate && python manage.py runserver

shell:
    source $(ENV)/bin/activate && python manage.py shell
```

### Usage
```
make setup
make migrate
make superuser
make run
make shell
```

---

## 📌 Notes
- Ensure PostgreSQL is installed and running.
- Always activate your virtual environment before running commands (unless using `make`).
- Keep your `.env` file out of version control.

---

## ✅ Next Steps
- Define models and migrations.
- Build modules (Inventory, Sales, HR, etc.).
- Add authentication & role-based permissions.
