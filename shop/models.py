from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=7,decimal_places=5)
    description = models.TextField(max_length=100)
    quantity = models.IntegerField()