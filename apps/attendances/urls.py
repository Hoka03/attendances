from django.urls import path

from apps.attendances.views import AttendanceCreateAPIView, AttendanceListAPIView, AttendanceUpdateAPIView, AttendanceDeleteAPIView


urlpatterns = [
    path('add/', AttendanceCreateAPIView.as_view()),
    path('', AttendanceListAPIView.as_view()),
    path('<int:pk>/', AttendanceUpdateAPIView.as_view()),
    path('delete/<int:pk>/', AttendanceDeleteAPIView.as_view())
]

