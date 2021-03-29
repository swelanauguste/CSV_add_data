from django.db import models

class Account(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name