from apps.users.models import CustomUser

from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    user_role = serializers.CharField(source='get_role_display', required=False)
    group = serializers.CharField(source='student_groups', required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'user_role', 'role', 'first_name', 'last_name', 'email', 'description', 'student_groups',
                  'group']
        extra_kwargs = {
            "role": {"write_only": True},
            "student_group": {"write_only": True},
        }

    def get_last_login(self, obj):
        return obj.last_login.strftime("%B %d %Y %H:%M:%S")  # time is for example

    def get_date_joined(self, obj):
        return obj.last_login.strftime("%B %d %Y")


class TeacherSerializer(serializers.ModelSerializer):
    user_role = serializers.CharField(source='get_role_display', required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'user_role', 'role', 'first_name', 'last_name', 'email', 'description', 'student_groups']
        extra_kwargs = {
            "role": {"write_only": True},
        }

    def get_last_login(self, obj):
        return obj.last_login.strftime("%B %d %Y %H:%M:%S")  # time is for example

    def get_date_joined(self, obj):
        return obj.last_login.strftime("%B %d %Y")
