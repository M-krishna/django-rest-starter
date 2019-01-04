from django.db import models

# Create your models here.
class SignUp(models.Model):
    firstname = models.CharField(max_length = 15)
    lastname = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 40)
    phone = models.CharField(max_length = 10)

    def __str__(self):
        return self.firstname + ' ' + self.lastname