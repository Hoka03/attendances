from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.groups.models import StudentGroup
from apps.groups.serializers import StudentGroupSerializer


class StudentGroupCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = StudentGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher_id = request.data.get('teacher')

        if StudentGroup.objects.filter(teacher_id=teacher_id).exists():
            return Response({'detail': 'Teacher is already assigned to another group.'}, status=400)

        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        groups = StudentGroup.objects.all().order_by('-id')
        many = True
        serializer = StudentGroupSerializer(groups, many=many)
        return Response(serializer.data, status=200)


class StudentGroupListAPIView(APIView):
    def get(self, request, pk):
        groups = get_object_or_404(StudentGroup, pk=pk)
        many = False
        serializer = StudentGroupSerializer(groups, many=many)
        return Response(serializer.data, status=200)


class StudentGroupUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        groups = get_object_or_404(StudentGroup, pk=pk)
        many = False
        serializer = StudentGroupSerializer(groups, many=many)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        groups = get_object_or_404(StudentGroup, pk=pk)
        serializer = StudentGroupSerializer(instance=groups, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class StudentGroupDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        groups = get_object_or_404(StudentGroup, pk=pk)
        many = False
        serializer = StudentGroupSerializer(groups, many=many)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        groups = get_object_or_404(StudentGroup, pk=pk)
        groups.delete()
        return Response(status=204)
