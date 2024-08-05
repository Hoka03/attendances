import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.utils.timezone import now

from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from config.settings.permissions import IsTeacherAndOwnGroup

from apps.attendances.serializers import Attendance, AttendanceSerializer
from apps.users.models import CustomUser


class AttendanceCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        if request.user.role == CustomUser.RoleChoices.TEACHER:
            if not request.data['student']:
                return Response({'student': 'This field is required'})

            group = request.user.teacher_group.first()
            student = get_object_or_404(get_user_model(), id=request.data['student'])
            if not student in group.students.all():
                return Response({'student': 'You don`t have permission for this group'})

        request.data['date'] = now().date()
        serializer = AttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class AttendanceListAPIView(APIView):

    def get(self, request):
        context = {}

        group_id = self.request.GET.get('group_id', '')
        year = self.request.GET.get('year', '')
        month = self.request.GET.get('month', '')

        if month.isdigit() and year.isdigit():
            days = list(range(1, calendar.monthrange(int(year), int(month))[1] + 1))
        else:
            days = []

        if group_id and month.isdigit() and year.isdigit():
            context['students'] = list(get_user_model().objects.filter(student_groups_id=group_id
                                                                       ).prefetch_related('student_attendance'
                                                                                          ).order_by('first_name'
                                                                                                     ).values('id',
                                                                                                              'first_name',
                                                                                                              'last_name'))
            attendances = list(Attendance.objects.filter(student__student_groups_id=group_id,
                                                         date__year=year,
                                                         date__month=month).values())
            for student in context['students']:
                student['attendances'] = []
                for day in days:
                    for attendance in attendances:
                        if attendance['date'].day == day and attendance['student_id'] == student['id']:
                            obj = {'come': attendance['come'], 'reason': attendance['reason'], 'day': day}
                            break
                    else:
                        obj = {'come': '', 'reason': '', 'day': day}
                    student['attendances'].append(obj)
        else:
            context['students'] = []

        if request.user.role == CustomUser.RoleChoices.TEACHER and group_id.isdigit() and int(group_id) != request.user.teacher_group.first().id:
            return Response({'message': 'You have not permission for this group'})

        return Response(context, status=200)


class AttendanceUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacherAndOwnGroup | IsAdminUser]

    def get(self, request, pk):
        attendances = get_object_or_404(Attendance, pk=pk)
        serializer = AttendanceSerializer(attendances, many=False)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        attendances = get_object_or_404(Attendance, pk=pk)
        serializer = AttendanceSerializer(instance=attendances, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'date' in request.data or 'student' in request.data:
            student_id = request.data.get('student', attendances.student_id)
            date = request.data.get('date', attendances.date)

            if Attendance.objects.filter(student_id=student_id, date=date).exclude(pk=pk).exists():
                return Response({'detail': 'Student has already been attendance on this date.'}, status=400)

        serializer.save()
        return Response(serializer.data, status=200)


class AttendanceDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        attendances = get_object_or_404(Attendance, pk=pk)
        many = False
        serializer = AttendanceSerializer(attendances, many=many)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        attendances = get_object_or_404(Attendance, pk=pk)
        attendances.delete()
        return Response(status=204)
