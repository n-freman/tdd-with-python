from django.db import models
from django.shortcuts import reverse


class List(models.Model):
    objects: models.Manager # for pyright

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id]) # type: ignore


class Item(models.Model):
    objects: models.Manager # for pyright
    text = models.TextField(default='')
    list = models.ForeignKey(
        List,
        default=None,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text

