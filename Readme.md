# Quizo - A Simple Django Quiz App

**Quizo** is a simple quiz application built using **Django**. The app allows users to answer quiz questions and select their preferred answers. This README will guide you through the setup and usage of the project.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Setup the Database](#setup-the-database)
4. [Running the Project](#running-the-project)
5. [Admin Interface](#admin-interface)

---

## Prerequisites

Before getting started, make sure you have the following installed:

- **Python** (version 3.6 or higher)
- **Django** (version 3.x or 4.x)

---

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/Quizo.git
    cd Quizo
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Make sure you have **Django** installed by running:

    ```bash
    python -m django --version
    ```

---

## Setup the Database

1. Make migrations for the database models:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Create a superuser account to access the admin interface:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set the username, email, and password for the superuser.

---

## Running the Project

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and go to `http://127.0.0.1:8000/` to start using the quiz app.

---

## Admin Interface

To manage questions and options easily, you can use Django's built-in admin interface:

1. Open the admin interface by visiting `http://127.0.0.1:8000/admin/` in your browser.
2. Log in using the superuser credentials you created.
3. You will find the **Questions** and **Options** models listed, where you can add new questions and their corresponding options.

---

## Project Structure

