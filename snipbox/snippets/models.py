from django.db import models

from core.models import AbstractDateBase, AbstractUserBase


class Tag(AbstractDateBase, AbstractUserBase):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Snippet(AbstractDateBase, AbstractUserBase):
    title = models.CharField(max_length=255)
    note = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
