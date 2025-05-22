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
   - If deploying to Render.com or another production server, you do not need to run the development server with `python manage.py runserver`. Instead, the platform will use the `Procfile` to start the app with Gunicorn automatically.
   - For local development, continue to use:
     ```sh
     python manage.py runserver
     ```

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

## Deployment on Render.com

To deploy on Render.com:
1. Make sure you have a `Procfile` in your project root with the following content:
   ```
   web: gunicorn webprep.wsgi:application --bind 0.0.0.0:$PORT
   ```
2. Set `ALLOWED_HOSTS` in `webprep/settings.py` to include your Render domain (e.g., `webprepwala.onrender.com`).
3. Render will automatically set the `PORT` environment variable. The above `Procfile` ensures Gunicorn binds to the correct port.
4. For static files, make sure to run:
   ```sh
   python manage.py collectstatic
   ```
5. For more details, see: https://render.com/docs/web-services#port-binding

## Notes
- Update `webprep/settings.py` for production (e.g., `ALLOWED_HOSTS`, `DEBUG`, database settings).
- For deployment, use a production-ready server (e.g., Gunicorn, Apache, Nginx).

## Contact
For any issues or questions, use the contact form on the website or email: webprepwala@gmail.com
