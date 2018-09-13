from unidecode import unidecode

from django.db import models
from django.utils.text import slugify


def post_upload_path(instance, filename):
    return 'blog/{}/image.jpg'.format(instance.title)


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=40)


class Post(models.Model):
    # TODO: validation on the title so that it is more easily URL-ized (no '/' and stuff)
    title = models.CharField(primary_key=True, unique=True, max_length=100)
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to=post_upload_path, blank=True)
    content = models.TextField(max_length=10000)
    briefing = models.TextField(max_length=1000)

    tags = models.ManyToManyField(Tag)

    # TODO: can I make this absent from the admin form rather than a default?
    slug = models.SlugField(max_length=140, unique=True, default="temp")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # TODO: ensure the slugified title is unique
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug
