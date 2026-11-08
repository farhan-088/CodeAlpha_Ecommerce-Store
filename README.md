# ShopEase — Simple E-commerce Store

A full-stack starter project for an internship task. ShopEase is a Django-based shopping website with product browsing, product detail pages, a session-based cart, account registration/login, checkout/order creation, and order history.

## Features

- Product catalog with search and category filter
- Product detail page
- Shopping cart: add, update quantity, remove items
- User registration and login/logout
- Authenticated checkout with delivery details
- Order history for logged-in users
- Stock validation and stock decrement at checkout
- Django Admin for product and order management
- Responsive HTML/CSS storefront
- SQLite database for local development

> **Note:** This project is for learning and demonstration. Checkout creates an order but does not accept or process payments.

## Tech stack

- Python
- Django
- SQLite
- HTML5, CSS3
- Django templates and session framework

## Run locally (Windows / VS Code)

### 1. Requirements
Install Python 3.11 or newer and VS Code.

### 2. Open this folder in VS Code
Open the `Simple_Ecommerce_Store_GitHub` folder. Use **Terminal → New Terminal**.

### 3. Create and activate virtual environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install packages

```powershell
pip install -r requirements.txt
```

### 5. Create database tables

```powershell
python manage.py makemigrations store
python manage.py migrate
```

### 6. Create administrator account

```powershell
python manage.py createsuperuser
```

### 7. Start development server

```powershell
python manage.py runserver
```

Visit:
- Store: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Add products

1. Log in to Django Admin.
2. Open **Products → Add Product**.
3. Add name, slug (unique URL name), description, price, stock, category, and optional image URL.
4. Set **Is active** to enabled and save.

Example demo catalog:
- Everyday Backpack — ₹1299 — stock 12 — category Accessories
- Wireless Headphones — ₹1999 — stock 8 — category Electronics
- Ceramic Coffee Mug — ₹299 — stock 20 — category Home

## GitHub upload

From this project folder, in the terminal:

```powershell
git init
git add .
git commit -m "Initial commit: ShopEase Django e-commerce store"
```

Create an empty repository on GitHub, then follow the repository page's instructions to connect the remote and push. Common commands:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your actual repository URL.

## Project structure

```text
Simple_Ecommerce_Store_GitHub/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── store/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/css/style.css
├── templates/
│   ├── base.html
│   ├── store/
│   └── registration/
├── manage.py
├── requirements.txt
└── README.md
```

## Security notes before deployment

- Set `DJANGO_SECRET_KEY` to a secure secret value.
- Set `DJANGO_DEBUG=False`.
- Set `DJANGO_ALLOWED_HOSTS` to your deployment host.
- Use a production database and HTTPS for deployment.
- Do not commit real credentials, `.env` files, or the local database.
