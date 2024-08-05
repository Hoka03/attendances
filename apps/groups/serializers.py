from rest_framework import serializers

from .models import StudentGroup


class StudentGroupSerializer(serializers.ModelSerializer):
    teacher_name = serializers.PrimaryKeyRelatedField(source='teacher.first_name', read_only=True)

    class Meta:
        model = StudentGroup
        fields = ['teacher', 'teacher_name', 'name', 'created_at']
        extra_kwargs = {
            "teacher": {"write_only": True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at.strftime("%Y-%m-%d")
        return representation
