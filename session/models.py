from django.db import models
from django.utils.text import slugify


class Session(models.Model):
    name=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    speaker=models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False, max_length=100)

    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        counter = 1

        while Session.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Session, self).save(*args, **kwargs)

    def __str__(self):
        return self.name