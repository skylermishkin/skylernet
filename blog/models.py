from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=40)


class Post(models.Model):
    title = models.CharField(primary_key=True, unique=True, max_length=100)
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField()
    content = models.TextField(max_length=10000)
    briefing = models.TextField(max_length=1000)
    tags = models.ManyToManyField(Tag)
