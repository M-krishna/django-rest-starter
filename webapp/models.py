from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model

# Create your models here.
class EmployeeModel(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname