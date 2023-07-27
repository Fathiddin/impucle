from django.db import models

# Create your models here.


class Registration(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    phone = models.IntegerField(unique=True)


    def __str__(self):
        return str(self.name)