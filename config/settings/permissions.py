from rest_framework.permissions import BasePermission


class IsTeacherAndOwnGroup(BasePermission):
    def has_permission(self, request, view):
        from apps.users.models import CustomUser  # Lazy import
        return request.user.is_authenticated and request.user.role == CustomUser.RoleChoices.TEACHER

    def has_object_permission(self, request, view, obj):
        return obj.student.student_group.teacher == request.user
