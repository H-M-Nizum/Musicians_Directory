from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=50)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f" {self.first_name} {self.last_name}"