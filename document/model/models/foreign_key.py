# ForeignKey로 2개의 class를 연결
from django.db import models

__all__ = (
    'Manufacturer',
    'Car',
    'User'
)


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.manufacturer.name} - {self.name}'


# 재귀관계 실습
class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
