from django.urls import path

from apps.users.views import students, teacher


urlpatterns = [
    path('students/', students.StudentCreateAPIView.as_view()),
    path('students/<int:pk>/', students.StudentListAPIView.as_view()),
    path('students/update/<int:pk>/', students.StudentUpdateAPIView.as_view()),
    path('students/delete/<int:pk>/', students.StudentDeleteAPIView.as_view()),
    # ======================== TEACHER ===========================
    path('teachers/', teacher.TeacherCreateAPIView.as_view()),
    path('teachers/<int:pk>/', teacher.TeacherListAPIView.as_view()),
    path('teachers/update/<int:pk>/', teacher.TeacherUpdateAPIView.as_view()),
    path('teachers/delete/<int:pk>/', teacher.TeacherDeleteAPIView.as_view()),
]
