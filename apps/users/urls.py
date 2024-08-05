from django.urls import path

from apps.users.views import students, teacher


urlpatterns = [
    path('students/', students.StudentListCreateAPIView.as_view()),
    path('students/<int:pk>/', students.StudentListCreateAPIView.as_view()),
    path('students/update/<int:pk>/', students.StudentUpdateAPIView.as_view()),
    path('students/delete/<int:pk>/', students.StudentDeleteAPIView.as_view()),
    # ======================== TEACHER ===========================
    path('teachers/', teacher.TeacherListCreateAPIView.as_view()),
    path('teachers/<int:pk>/', teacher.TeacherListCreateAPIView.as_view()),
    path('teachers/update/<int:pk>/', teacher.TeacherUpdateAPIView.as_view()),
    path('teachers/delete/<int:pk>/', teacher.TeacherDeleteAPIView.as_view()),
]
