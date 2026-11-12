# Django Student & Recipe CRUD Application

A full-stack web application built with **Django** and connected to a cloud **MySQL** database (Aiven). This project features user registration, a contact messaging system, and complete **CRUD (Create, Read, Update, Delete)** operations for managing Students and Recipes.

---

## Features

* **User Registration (`/register/`):** Allows new users to sign up with password matching validation, duplicate username checks, and automatic password hashing.
* **Student Management CRUD (`/students/`):** Create, view, update, and delete student records (Full Name, Registration Number, Email, and Course).
* **Recipe Management CRUD (`/recipes/`):** Create, view, update, and delete recipe entries.
* **Contact Form (`/contact/`):** Stores visitor inquiries directly into the MySQL database.
* **Shared Navigation & Styling:** Responsive navigation bar (`navbar.html`) and custom CSS styling across all pages.
* **Django Admin Panel (`/admin/`):** Full administrative dashboard registered for managing Users, Students, Recipes, and Contact Messages.
* **Cloud MySQL Database:** Configured to store and retrieve live data from an Aiven MySQL server using environment variables (`.env`) for credential security.

---

## Tech Stack

* **Backend:** Python, Django
* **Database:** MySQL (Hosted on Aiven)
* **Frontend:** HTML5, CSS3, Django Template Engine

---

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd django-student-crud
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django mysqlclient
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your database password:
   ```env
   DB_PASSWORD=your_mysql_password
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser:**
   * Registration: `http://127.0.0`
   * Students CRUD: `http://127.0.0`
   * Recipes CRUD: `http://127.0.0`
   * Contact Us: `http://127.0.0`
   * Admin Dashboard: `http://127.0.0`
