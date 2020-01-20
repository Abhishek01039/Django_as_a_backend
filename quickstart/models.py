from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
