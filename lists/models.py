from django.db import models
from django.shortcuts import reverse


class List(models.Model):
    objects: models.Manager # for pyright

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    objects: models.Manager # for pyright
    text = models.TextField(default='')
    list = models.ForeignKey(
        List,
        default=None,
        on_delete=models.CASCADE
    )

