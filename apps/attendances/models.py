from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

from apps.users.models import CustomUser


class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                limit_choices_to={'role': CustomUser.RoleChoices.STUDENT.value},
                                related_name='student_attendance')
    come = models.BooleanField(default=True)
    date = models.DateTimeField()
    reason = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('student', 'date')

    def clean(self):
        if Attendance.objects.filter(student=self.student, date=self.date).exists():
            raise ValidationError('Attendance for this student on this date already exists')
        super().clean()
        
    def __str__(self):
        return f'{self.student} - {self.date}'
