from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40, unique=True)
    email = models.EmailField(verbose_name="email", max_length=40, unique=True)
    password=models.CharField(max_length=30)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	
    def __str__(self):
        return self.name