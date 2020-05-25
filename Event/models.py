from django.db import models
from django.utils.text import slugify
from session.models import Session
from timezone_field import TimeZoneField
import pytz


class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES)
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, editable=False, max_length=100)

    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        counter = 1

        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1
        return unique_slug

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Event, self).save(*args, **kwargs)

