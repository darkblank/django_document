from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name
