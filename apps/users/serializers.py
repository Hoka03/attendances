from apps.users.models import CustomUser

from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['role', 'first_name', 'last_name', 'email', 'description', 'student_groups']

    def get_last_login(self, obj):
        return obj.last_login.strftime("%B %d %Y %H:%M:%S")  # time is for example

    def get_date_joined(self, obj):
        return obj.last_login.strftime("%B %d %Y")


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['role', 'first_name', 'last_name', 'email', 'description', 'student_groups']

    def get_last_login(self, obj):
        return obj.last_login.strftime("%B %d %Y %H:%M:%S")  # time is for example

    def get_date_joined(self, obj):
        return obj.last_login.strftime("%B %d %Y")
