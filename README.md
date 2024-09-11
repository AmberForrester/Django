<a id="readme-top"></a>

<h1 align='center'>Django :zap:</h1>

## Typical Project Structure:
Keeping in mind Django's best practices, this will help make a Django project more Modular to:
- Separate concerns
- Organize code efficiently
- Creates structured scalablity 
- Keeps project manageable as it grows 

Example:<br/>
/named_venv_folder/<br/>
    |-- /your_project/          ***Root Folder of the Django project***<br/>
    |       |-- __init__.py     ***Makes this a Python package***<br/>
    |       |-- settings.py     ***Project level settings***  <br/>
    |       |-- urls.py         ***Project level URL configurations***<br/>
    |       |-- wsgi.py         ***WSGI entry point for production servers***<br/>
    |       |-- asgi.py         ***ASGI entry point for async handling***<br/>
    |<br/>
    |<br/>
    |<br/>
    |-- /apps/   ***Custom folder for your apps (if you have multiple apps)<br/>
    |       |-- /app_name/              ***Individual Django App***<br/>
    |       |       |-- migrations/     ***Database migration files***<br/>
    |       |       |-- templates/      ***App specific templates***<br/>
    |       |       |-- static/         ***App specific static files (CSS, JS, favicon, images)***<br/>
    |       |       |-- admin.py/       ***App admin panel configuartion***<br/>
    |       |       |-- apps.py/        ***App configuration***<br/>
    |       |       |-- models.py/      ***Database models***<br/>
    |       |       |-- urls.py/        ***App specific URLs***<br/>
    |       |       |-- views.py/       ***Views handling logic***<br/>
    |       |       |-- forms.py/       ***Forms related to the App***<br/>
    |       |       |-- tests.py/       ***Tests related to the App***<br/>
    |<br/>
    |<br/>
    |<br/>
    |-- /static/            ***Project level static files (CSS, JS, favicon, images)***<br/>
    |-- /templates/         ***Project level templates (ex. master.html)***<br/>
    |-- /media/             ***For media files (if you are working with file uploads)***<br/>
    |-- manage.py           ***Django's management script***<br/>
    |-- requirements.py     ***List of dependencies for the project***<br/>



## Steps to Organize Project Modularly

1. ### Create an "apps" folder:
If you have multiple Django apps (such as blogs, accounts, job listings, etc.), you can place them into a folder called `/apps/` to logically group them. 

Making it easier to manage many apps. 

Example:<br/>
/your_project/<br/>
    |-- /apps/<br/>
            |-- blog/<br/>
            |-- accounts/<br/>
            |-- joblistings/<br/>

2. ### Move static files to app-specific folders:
For each app, create a `/static/` folder within the app directory and move the static files (CSS, JS, images) that are related to that app into this folder. 

This keeps static files organized by app. 

Example: <br/>
/apps/blog/static/blog/css<br/>
/apps/blog/static/blog/js<br/>

3. ### Move templates to app-specific folders:
Inside each app, create a `/templates/` folder for templates specific to that app.

This avoids confusion, especially when multiple apps have similary named templates.

Example:<br/>
/apps/blog/templates/blog/index.html<br/>

4. ### Centralize shared templates and static files:
You can keep shared templates (ex. master.html layout) and shared static files (like global CSS or JavaScript) in the root `templates/` and `/static/` folders, respectively because they will be used across multiple apps. 

5. ### Modularize settings (Optional):
If your project grows, you can split the `settings.py` file into multiple files, such as `base.py`, `dev.py`, and `prod.py`, for easier management of development and production settings. 

Example:<br/>
/your_project/settings/<br/>
    |-- base.py<br/>
    |-- dev.py<br/>
    |-- prod.py<br/>

6. ### Forms and Tests:
If you are using forms and writing tests, keep `forms.py` and `tests.py` inside each app directory to encapsulate the logic for that app. 

7. ### Media Files (optional):
If your project involves user uploads (like images or files), consider adding a `/media/` directory to store those uploaded files. 

Django will use this folder to serve media files when properly configured. 

Once you move things around:
- Update the `INSTALLED_APPS` in your `settings.py` to reflect the new app structure (ex. `apps.blog` instead of just `blog`).

- Update any import statements in your project to match the new structure (for example, when importing models or views).




<p align="right">(<a href="#readme-top">top of page</a>)</p>