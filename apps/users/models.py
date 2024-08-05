from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    class RoleChoices(models.IntegerChoices):
        ADMIN = 1, 'Admin'
        TEACHER = 2, 'Teacher'
        STUDENT = 3, 'Student'

    objects = CustomUserManager()
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    role = models.PositiveSmallIntegerField(choices=RoleChoices.choices)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    description = models.TextField(max_length=1500)

    student_groups = models.ForeignKey('groups.StudentGroup', on_delete=models.CASCADE, related_name='students',
                                       blank=True, null=True)

    def __str__(self):
        return self.first_name
