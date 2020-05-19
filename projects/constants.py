from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusCode(models.TextChoices):
    PENDING = 'P', _('Pending')
    TBD = 'TBD', _('To-Be-Disscussed')
    RESOLVED = 'R', _('Resolved')


Client_ID = 'bJJ0mJGuqBJRfU45hBECxOFO6XkvqD3HuuMAajB4'

Client_secret = 'Af8sNUBrosjmYdBJEcKgT9ysguy6MVuKcFBQtVAkNRmvtw68zPdPI0NHpCcA7dMQamayX16KjXdI1u8kjT9ic47qp7MAEl8EgOwOyTgRR9zsq4I9z7Qea0i4fokvnlU0'

Redirect_Url = "http://localhost:3000/"

Access_Token_Endpoint = "https://internet.channeli.in/open_auth/token/"

user_data = {
    "userId": 6283,
    "person": {
        "shortName": "",
        "fullName": "Rohit Aggarwal",
        "roles": [
            {
                "role": "Student",
                "activeStatus": "ActiveStatus.IS_ACTIVE"
            },
            {
                "role": "Maintainer",
                "activeStatus": "ActiveStatus.WILL_BE_ACTIVE"
            }
        ],
        "displayPicture": "null"
    },
    "student": {
        "enrolmentNumber": "19116069",
        "currentYear": 1
    },
    "contactInformation": {
        "emailAddress": "rudrakgarwalsachin@gmail.com"
    }
}
