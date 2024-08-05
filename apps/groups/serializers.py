from rest_framework import serializers

from .models import StudentGroup


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ['teacher', 'name', 'slug', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at.strftime("%Y-%m-%d")
        return representation
