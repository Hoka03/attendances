from rest_framework import serializers

from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.first_name', read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date'] = instance.date.strftime("%Y-%m-%d")
        return representation
