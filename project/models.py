from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"ID: {self.pk} | Username: {self.username}"