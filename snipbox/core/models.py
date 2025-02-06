from django.conf import settings
from django.db import models


class AbstractDateBase(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractUserBase(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='%(class)s_createdby',
                                   blank=True, on_delete=models.CASCADE)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='%(class)s_modifiedby',
                                    null=True, blank=True,
                                    on_delete=models.CASCADE)

    class Meta:
        abstract = True
