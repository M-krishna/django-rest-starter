from django.db import models

# Create your models here.
class StudentModel(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname