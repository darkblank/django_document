from django.db import models


# Create your models here.
# choice 실습
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


# primary_key를 "id"가 아닌 다른 값으로 쓰고싶을 때
class Fruit(models.Model):
    name = models.CharField(
        max_length=100,
        primary_key=True
    )


# ForeignKey로 2개의 class를 연결
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
