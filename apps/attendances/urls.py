from django.urls import path

from apps.attendances.views import AttendanceListCreateAPIView, AttendanceUpdateAPIView, AttendanceDeleteAPIView


urlpatterns = [
    path('add/', AttendanceListCreateAPIView.as_view()),
    path('<int:pk>/', AttendanceUpdateAPIView.as_view()),
    path('delete/<int:pk>/', AttendanceDeleteAPIView.as_view())
]

