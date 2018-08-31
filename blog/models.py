from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=100)
    image = models.ImageField()
    author = models.TextField(max_length=20)
    date_posted = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=10000)
