# WebPrepWala Website

This is a Django-based website for WebPrepWala. Follow the instructions below to set up, run, and use the website locally.

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Virtual environment tool (e.g., `venv` or `virtualenv`)

## Setup Instructions

1. **Clone or Download the Project**
   - Place the project folder on your local machine.

2. **Navigate to the Project Directory**
   ```sh
   cd path/to/web123
   ```

3. **Create and Activate a Virtual Environment (Recommended)**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install Dependencies**
   - If a `requirements.txt` file exists:
     ```sh
     pip install -r requirements.txt
     ```
   - If not, install Django manually:
     ```sh
     pip install django
     ```

5. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

6. **Create a Superuser (Optional, for Admin Access)**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   - The website will be available at `http://127.0.0.1:8000/`

## Using the Website
- Visit the home page at `http://127.0.0.1:8000/`
- Navigate to different sections using the menu (Home, About, Portfolio, Contact, etc.)
- To use the contact form, go to `/contact/`, fill in the form, and submit your query.
- For admin access, go to `/admin/` and log in with your superuser credentials.

## Static Files
- Static files (CSS, images, JS) are located in the `static/` directory.
- To collect static files for production, run:
  ```sh
  python manage.py collectstatic
  ```

## Notes
- Update `webprep/settings.py` for production (e.g., `ALLOWED_HOSTS`, `DEBUG`, database settings).
- For deployment, use a production-ready server (e.g., Gunicorn, Apache, Nginx).

## Contact
For any issues or questions, use the contact form on the website or email: webprepwala@gmail.com
