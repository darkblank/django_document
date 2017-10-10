from django.db import models

__all__ = (
    'Fruit'
)


# primary_key를 "id"가 아닌 다른 값으로 쓰고싶을 때
class Fruit(models.Model):
    name = models.CharField(
        max_length=100,
        primary_key=True
    )
