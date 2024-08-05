from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.users.serializers import StudentSerializer
from apps.users.models import CustomUser


class StudentCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        request.data['role'] = 3
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if CustomUser.objects.filter(email=request.data['email']).exists():
            return Response({'detail': 'Student with this email already exists.'},
                            status=400)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        students = CustomUser.objects.filter(role=CustomUser.RoleChoices.STUDENT).order_by('-id')
        many = True
        serializer = StudentSerializer(students, many=many)
        return Response(serializer.data, status=200)


class StudentListAPIView(APIView):
    def get(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        many = False
        serializer = StudentSerializer(students, many=many)
        return Response(serializer.data, status=200)


class StudentUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        many = False
        serializer = StudentSerializer(students, many=many)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        serializer = StudentSerializer(instance=students, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if 'student_group' in request.data:
            if CustomUser.objects.filter(student_group=request.data['student_group']).exclude(pk=pk).exists():
                return Response({'detail': 'Student is already assigned to other group.'},
                                status=400)
        serializer.save()
        return Response(serializer.data, status=200)


class StudentDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        many = False
        serializer = StudentSerializer(students, many=many)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        students = get_object_or_404(CustomUser, pk=pk)
        students.delete()
        return Response(status=204)

