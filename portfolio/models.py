from unidecode import unidecode

from django.db import models
from django.utils.text import slugify


def project_upload_path(instance, filename):
    return 'portfolio/{}/image.jpg'.format(instance.title)


class Project(models.Model):
    title = models.CharField(primary_key=True, unique=True, max_length=100)
    image = models.ImageField(upload_to=project_upload_path)
    short = models.CharField(max_length=1000)
    long = models.TextField(max_length=10000)
    live_url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=100, unique=True, default='auto')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # TODO: more slug validation
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
