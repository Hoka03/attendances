from django.db import models

from .services import normalize_text


class AbstractModel(models.Model):
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
