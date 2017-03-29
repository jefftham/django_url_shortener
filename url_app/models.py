from django.db import models
import random, string

max_short_length = 8


def random_short():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(max_short_length))


# Create your models here.
class Url_table(models.Model):
    full = models.URLField(max_length=500)
    short = models.CharField(max_length=max_short_length, unique=True, default=random_short)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.short

    class Meta:
        ordering = ['-count']
