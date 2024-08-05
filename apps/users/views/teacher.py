from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.users.serializers import TeacherSerializer
from apps.users.models import CustomUser


class TeacherListCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        students = CustomUser.objects.all().order_by('-id')
        many = True
        serializer = TeacherSerializer(students, many=many)
        return Response(serializer.data, status=200)


class TeacherUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        many = False
        serializer = TeacherSerializer(students, many=many)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        serializer = TeacherSerializer(instance=students, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class TeacherDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        many = False
        serializer = TeacherSerializer(students, many=many)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        students.delete()
        return Response(status=204)

