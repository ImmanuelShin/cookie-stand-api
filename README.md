# Lab - Class 34

## Project: Cookie Stand

### Author: [Immanuel Shin](https://github.com/ImmanuelShin)

A small web project that ties together Django and DRF to create a front facing website and a backend remote database.

### Setup

#### Requirements

**How to initialize/run your application:**

  1. Clone the repository.
   ```bash
   git clone
   ```
  2. Navigate to the project directory.
   ```bash
   cd [name-of-directory]
   ```
  3. Activate your virtual environment (if applicable).
   ```bash
   `python3 -m venv .venv`

   `source .venv/bin/activate` (Linux/Mac)

   `source .venv/Scripts/activate` (Windows)
   ```
  4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
  5. Apply migrations:
  ```bash
  python manage.py migrate
  ```
  6. Run server with `python manage.py runserver`
  7. Visit webpage at 127.0.0.1:8000