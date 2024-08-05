from django.db import models
from django.conf import settings

from apps.users.models import CustomUser


class StudentGroup(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                limit_choices_to={'role': CustomUser.RoleChoices.TEACHER.value})
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
