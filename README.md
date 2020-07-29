# BUG MANAGER BACKEND

Bug Tracker is an app that aids in tracking bugs, issues, and questions in any app development. It provides a collaborative environment for the team to solve the issues related to the project.

**Built with**:

- Django
- Django Rest Framework

## SETUP

---

- Requirements

  - pip
  - Python3
  - Virtual Environment
  - Redis Server

- Clone this repo.
- Setup and activate your virtual environment.
- Navigate inside the cloned repository and install the required dependencies using the command:

```
pip install -r requirements.txt
```

- Now in navigate to /bugmanager and create a file named credentials.py having the following content:

```EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = your_email
EMAIL_HOST_PASSWORD = your_password
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```

- Navigate back to base directory and make migrations using the following command:

```
python manage.py migrate
```

- Make sure Redis Server is running on port 6379.
- Finally run the following command:

```
python manage.py runserver
```

- Go to [this url](http://localhost:8000/admin) to confirm your backend is setup properly.
