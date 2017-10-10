from django.db import models

__all__ = (
    'Pizza',
    'Topping',
    'FacebookUser',
    'InstagramUser',
)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField('Topping', blank=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class FacebookUser(models.Model):
    name = models.CharField(max_length=30)
    twitterusers = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name


class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name
