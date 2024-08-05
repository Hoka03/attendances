from django.urls import path

from apps.groups.views import StudentGroupListCreateAPIView, StudentGroupUpdateAPIView, StudentGroupDeleteAPIView


urlpatterns = [
    path('', StudentGroupListCreateAPIView.as_view()),
    path('<int:pk>/', StudentGroupListCreateAPIView.as_view()),
    # ==================== UPDATE ==================
    path('update/<int:pk>/', StudentGroupUpdateAPIView.as_view()),
    # ==================== DELETE =====================
    path('delete/<int:pk>/', StudentGroupDeleteAPIView.as_view())
]
