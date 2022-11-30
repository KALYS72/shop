from django.db import models

class Post(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()

