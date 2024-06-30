from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = (
    ('male','Male'),
    ('female','Female'),
)

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=6,choices=GENDER,default='male')
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)

