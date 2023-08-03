# Django Essential Training (LinkedIn course)
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/487c16429ab871792d39017fd5d948071ea8e40b89efb37e2456c47875fd5c5e)

In this course, you will learn how to create web applications using Django, a popular Python web framework. You will learn the basics of Django, such as how to use the Model-View-Template (MVT) design pattern, how to handle requests and responses, how to work with templates and databases, and how to create multiple apps within a project.

### What you need:

- Python 3.8 virtualenv
- Django 3.2
- Code editor
- Browser (Chrome)
- Familiarity with HTTP and its methods

### Create a new Django project:

1. Use the `django-admin startproject [name of the project]` command to create a folder of the project name and a `manage.py` file, which is the entry point of the project. You can run the project server through it.
2. Inside the project folder `smartnotes`, there are the configuration files.
3. In `settings.py`, there are many global variables defined. For example, `DEBUG = True` means that we are working in a development environment.
4. Now you can run the project using `python manage.py runserver` to run the server using the default configuration

### Create a minimum working page => First view:

1. Use the `django-admin startapp home` command to create a new app called `home`.
2. Every time you create an app, you need to add it to the `settings.py` file, so Django knows that this folder is part of the project. Under `INSTALLED_APPS`, add `'home',`.
3. Now you can start creating the first view of the project. Go to `home/views.py` and write your first function, which is a preconfigured file.
4. To know when to send requests for any function, you can go to `smartnotes/urls.py` file and import that file there to have access.
5. In `urls.py` in `smartnotes` folder, add the following: `from home import views` and inside `urlpatterns`, add a new path: `path('home', views.home)`.
6. Now if you run `python manage.py runserver` in localhost, you will see a `404` error, but you can still see the admin and home endpoints.
![see the image](images/404.png "First Image")
7. When you go to `/home` endpoint, you are making a request to that path, so Django will go to `urls.py` to see if it is ready to receive a request at this path. If it is, it will go to `views.py` file and then to the `def home` function. When the function receives the request, it will respond with its content, which is `Hello world` in our case.
![see the image](images/Function.png "Second Image")
![see the image](images/home.png "Third Image")
8. Django uses the Model-View-Template (MVT) pattern, which is similar to the Model-View-Controller (MVC) pattern. In MVT, the model is the data layer that defines the structure and logic of the data. The view is the presentation layer that handles the user interface and interaction. The template is the HTML file that renders the view with dynamic data.

### Build the Django project => Template:

1. Create a folder called `templates` and inside it create another folder and name it as the app's name: `home`.
2. Inside `/templates/home`, create a file called `welcome.html` and inside it add a basic HTML page.
3. Go to `views.py` and use the function `render`.
4. The empty brackets are a way to pass down information from view to template: `{}`.
5. Pass the datetime module to pass today's date in the dictionary with a key called today.

### Apps and modularization:

1. You can have as many apps as you want, but organize them so each app is self-contained.
2. Create another `urls.py` file inside home app that is similar to the one we have in the smartnotes app. Use `include`.
3. Now if you delete the whole app, it will not give you any errors because the app is not imported in the smartnotes urls file, but by its own urls.

### Creating Users in Django

Django has its own authentication system that allows us to create, delete and manage users. We can also use the Django admin interface to access and modify the data in the database.

#### Using the admin interface

- The admin endpoint is available at `/admin` and has its own authentication system.
- To access the admin interface, we need to create a super user using the command `python manage.py createsuperuser`.
- The admin interface allows us to create, edit and delete users, as well as other models that we register in the `admin.py` file of each app.
- Django admin is highly configurable and customizable.

#### Using migrations

- Migrations are files that explain what types of changes need to be applied to the database, such as creating, modifying or deleting tables or columns.
- To create migrations, we use the command `python manage.py makemigrations`.
- To apply migrations, we use the command `python manage.py migrate`.
- Migrations help us keep track of the changes in the database schema and make it easy to sync the database with the models.

### Interaction with Database

Django uses an ORM (Object Relational Mapping) system that allows us to work with the database using Python classes and objects.

#### Creating models

- A model is a Python class that represents a table in the database. The attributes of the class are the columns of the table.
- To create a model, we need to create an app using the command `django-admin startapp <app_name>`.
- Then, we need to add the app to the `INSTALLED_APPS` list in the `settings.py` file of the project.
- Next, we need to define the model class in the `models.py` file of the app, inheriting from `django.db.models.Model`.
- Finally, we need to create and apply migrations using the commands `python manage.py makemigrations` and `python manage.py migrate`.

#### Working with models

- To work with models through code, we can use the `python manage.py shell` command, which gives us an interactive interpreter that is connected to the current project.
- From the shell, we can import the models and use methods such as `.objects.create()`, `.objects.filter()`, `.objects.get()`, `.save()`, `.delete()` and others to manipulate the data in the database.
- We can also use query sets, which are collections of objects that can be filtered, ordered, sliced and aggregated.

### Building Dynamic Webpages

Django allows us to build dynamic webpages using views and templates.

#### Creating views

- A view is a Python function or class that handles a request and returns a response.
- To create a view, we need to define it in the `views.py` file of the app, using either a function-based view or a class-based view.
- A function-based view takes a request object as an argument and returns a response object, usually using the `render()` shortcut function.
- A class-based view inherits from a generic view class, such as `ListView`, `DetailView`, `CreateView`, etc., and overrides some attributes and methods to customize its behavior.
- To make a view accessible from a URL, we need to add it to the `urls.py` file of the app, using either the `path()` or `re_path()` function.
- Then, we need to include the app's URLs in the project's `urls.py` file, using the `include()` function.

#### Creating templates

- A template is an HTML file that can contain variables, tags and filters that are rendered by Django into a final webpage.
- To create a template, we need to create a folder named `templates` inside the app folder, and then create another folder with the same name as the app inside it.
- Then, we need to create an HTML file inside that folder with any name we want.
- In the template, we can use variables such as `{{ variable }}` to display values passed from the view, tags such as `{% tag %}` to perform logic or control flow, and filters such as `{{ variable|filter }}` to modify or format values.
- We can also use template inheritance to reuse common parts of templates, such as headers or footers. To do that, we need to create a base template that contains `{% block %}` tags for sections that can be overridden by child templates. Then, we need to use `{% extends %}` tag in child templates to inherit from the base template and `{% block %}` tags to fill in or override sections.

#### Handling errors

- Sometimes, errors may occur when handling requests or rendering templates. Django provides some built-in error pages for common errors such as 404 (page not found) or 500 (internal server error).
- We can customize these error pages by creating templates named `404.html` or `500.html` in the `templates` folder of the project (not the app).
- We can also use the `DEBUG` setting in the `settings.py` file to control whether to show detailed error messages or not. When `DEBUG` is `True`, Django will show a traceback and a debug toolbar for errors. When `DEBUG` is `False`, Django will show the custom error pages if they exist, or the default ones otherwise.

### Building Frontend with Django

1. **static folder:** Create a `static` folder to store static files like CSS, JavaScript, and images.
2. **CRUD operations:** Implement CRUD (Create, Retrieve, Update, Delete) operations for your models.
3. **Create a form:** Build a form to handle user input and validate data.
4. **Cross-Site Request Forgery (CSRF):** Use CSRF protection to prevent third-party attacks by sending and validating tokens.
5. **Update endpoint:** Set up update endpoints to modify existing data.
6. **Deleting data:** Implement deletion functionality to allow users to delete data.

#### Store and Display User-Specific Data

1. **Foreign keys:** Use Foreign Keys to establish relationships between models. For example, in `notes/models.py`, you can import `User` and add a field `user` as a ForeignKey to relate notes to a specific user.
2. **Migrations:** When modifying a model, create a migration using `python manage.py makemigrations` and apply the changes to the database with `python manage.py migrate`.
3. **Testing migrations:** To test if the migration works, open the Django shell using `python manage.py shell`, import the `User` model, and retrieve a user instance by calling `User.objects.get(pk=1)` or any other existing user ID. You can count the number of notes for a specific user using `user.notes.count()` or get all the notes for that user using `user.notes.all()`.
4. **Authentication:** Implement authentication to ensure user privacy and security.
5. **Class-based views:** Consider using class-based views, as they are powerful and customizable for handling different scenarios. For a comprehensive list of Django's class-based views, refer to [ccbv.co.uk/projects/Django/3.1/django.views.generic.list/ListView/](ccbv.co.uk/projects/Django/3.1/django.views.generic.list/ListView/).
6. **Form handling:** When handling user-submitted data, it passes through a form that validates it using methods like `clean_title` and `clean_text`. If any errors are encountered, the form raises an error, and if everything is valid, the data is stored in the `cleaned_data` variable and then saved to the database using `save()`.
7. **Database constraints:** Ensure that the database prevents saving a note without a corresponding user.

### Login, Logout Made Simple

1. **Authentication interfaces:** Create authentication interfaces to allow users to log in and log out.
2. **Custom settings:** Django provides pre-configured settings for actions after login, and you can customize them in the settings.
3. **Login and logout endpoints:** Implement endpoints for login and logout, and then proceed to create a signup page.
4. **Signup restrictions:** To ensure only non-logged-in users can access the signup page, override the `get` method and redirect the user if they are already logged in.

> Remember to read the Django documentation thoroughly and consider exploring other courses to deepen your understanding and skills in Django development. The Django documentation provides comprehensive and up-to-date information on all aspects of Django development.
