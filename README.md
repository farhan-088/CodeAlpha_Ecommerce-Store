# ShopEase — Simple E-commerce Store

A full-stack Django-based e-commerce website developed as an internship project. ShopEase allows users to browse products, view product details, add products to a shopping cart, register/login, checkout, and view their order history.

## Features

- Product catalog with search and category filtering
- Product detail pages
- Shopping cart with add, update quantity, and remove functionality
- User registration and login/logout
- Authenticated checkout with delivery details
- Order history for logged-in users
- Stock validation and stock decrement during checkout
- Django Admin panel for product and order management
- Responsive HTML/CSS storefront
- SQLite database for local development

> **Note:** This project is for learning and demonstration purposes. Checkout creates an order but does not accept or process payments.

## Tech Stack

- Python 3.11+
- Django
- SQLite
- HTML5
- CSS3
- Django Templates
- Django Session Framework

## Project Structure

```text
Simple_Ecommerce_Store_GitHub/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   ├── store/
│   └── registration/
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Run Locally (Windows / VS Code)

Follow these steps to run the ShopEase E-commerce Store on your computer.

### 1. Requirements

Install the following:

- Python 3.11 or newer
- Visual Studio Code
- Git

### 2. Clone the Repository

Open the VS Code terminal and run:

```bash
git clone https://github.com/farhan-088/CodeAlpha_Ecommerce-Store.git
```

Navigate to the project directory:

```bash
cd CodeAlpha_Ecommerce-Store
```

### 3. Create a Virtual Environment

```powershell
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```powershell
python -m pip install --upgrade pip
```

```powershell
pip install -r requirements.txt
```

### 6. Create Database Tables

Run the following command:

```powershell
python manage.py migrate
```

This command creates the required database tables using the migration files included in the repository.

### 7. Create an Administrator Account (Optional)

```powershell
python manage.py createsuperuser
```

Enter your username, email address, and password when prompted.

### 8. Start the Development Server

```powershell
python manage.py runserver
```

### 9. Open the Website

Store Website:

http://127.0.0.1:8000/

Django Admin Panel:

http://127.0.0.1:8000/admin/

Keep the terminal running while using the website.

To stop the server, press `Ctrl + C` in the terminal.

## Add Products

To add products to the store:

1. Open the Django Admin Panel.
2. Log in using your administrator account.
3. Open **Products**.
4. Click **Add Product**.
5. Enter product details.
6. Set the product as active.
7. Save the product.

Example Demo Catalog:

| Product | Price | Stock | Category |
|---|---:|---:|---|
| Everyday Backpack | ₹1299 | 12 | Accessories |
| Wireless Headphones | ₹1999 | 8 | Electronics |
| Ceramic Coffee Mug | ₹299 | 20 | Home |

## Database

ShopEase uses SQLite for local development.

The database tables are created by running:

```powershell
python manage.py migrate
```

If you encounter an error such as:

```text
OperationalError: no such table: store_product
```

Run:

```powershell
python manage.py migrate
```

Then restart the development server.

## GitHub Repository

GitHub Repository:

https://github.com/farhan-088/CodeAlpha_Ecommerce-Store

To upload any new changes:

```powershell
git add .
git commit -m "Update ShopEase project"
git push
```

## Security Notes Before Deployment

Before deploying the project to a production environment:

- Set `DJANGO_SECRET_KEY` to a secure secret value.
- Set `DJANGO_DEBUG=False`.
- Configure `DJANGO_ALLOWED_HOSTS` for your deployment domain.
- Use a production database.
- Enable HTTPS.
- Do not commit real credentials or `.env` files.
- Do not expose sensitive user information.

## Future Enhancements

- Online payment gateway integration
- Product reviews and ratings
- Wishlist functionality
- Order tracking
- Product image upload
- Email notifications
- Deployment to a cloud hosting platform

## Author

Developed as an internship project.

## License

This project is intended for educational and demonstration purposes.