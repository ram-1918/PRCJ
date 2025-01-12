from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True, max_length = 255)
    password = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    phone  = models.CharField(max_length=10)

    def __str__(self):
        return self.name+" "+self.email