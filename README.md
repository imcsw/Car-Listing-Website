# Car-Listing-Website
Car Listing Website created using Python programming language and Django framework using SQLite as the database.

# Instructions
<b>You will need to install Pyenv (version management for Python), DB Browser (SQLite database management software), and Python (version should not matter, but just in case it doesnt work, I developed it using v3.9.6)</b>

The libraries used for this project are as follows:
- Bootstrap 5
- DataTables
- django-crispy-forms
- Python Imaging Library (Pillow)
- django-simple-captcha

The website can be started by typing “<i>python manage.py</i>” in the command prompt. By default, the server will be running on port number 8000, you can specify the port of the server by appending the port number at the back of the command. Make sure that the command prompt is pointing to the project’s root directory. The URL to access the website is <i>http://127.0.0.1:8000/</i> if the port number was left on default. 

# Admin Page Access
You may access the admin page by using <i>admin</i> as the username and password.

Alternatively, you can add your own account by registering on the website first, then open up the SQLite file on DB Browser. Navigate to the <i>auth_user</i> table and change the value of <i>is_superuser</i> and <i>is_staff</i> to 1. Save changes and exit once done.
