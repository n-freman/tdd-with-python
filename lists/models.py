from django.db import models


class List(models.Model):
    objects: models.Manager # for pyright


class Item(models.Model):
    objects: models.Manager # for pyright
    text = models.TextField(default='')
    list = models.ForeignKey(
        List,
        default=None,
        on_delete=models.CASCADE
    )
