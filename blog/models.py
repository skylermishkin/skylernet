from django.db import models


def post_upload_path(instance, filename):
    return 'blog/{}/image.jpg'.format(instance.title)


class Tag(models.Model):
    tag_name = models.CharField(max_length=40)


class Post(models.Model):
    title = models.CharField(primary_key=True, unique=True, max_length=100)
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to=post_upload_path)
    content = models.TextField(max_length=10000)
    briefing = models.TextField(max_length=1000)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
