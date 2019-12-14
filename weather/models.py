from django.db import models
from django.core.validators import validate_email


class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.city + ', ' + self.state

class Email(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=100, unique=True,validators=[validate_email])