from django.urls import path

from apps.groups.views import (StudentGroupCreateAPIView, StudentGroupListAPIView, StudentGroupUpdateAPIView,
                               StudentGroupDeleteAPIView)


urlpatterns = [
    path('', StudentGroupCreateAPIView.as_view()),
    path('<int:pk>/', StudentGroupListAPIView.as_view()),
    # ==================== UPDATE ==================
    path('update/<int:pk>/', StudentGroupUpdateAPIView.as_view()),
    # ==================== DELETE =====================
    path('delete/<int:pk>/', StudentGroupDeleteAPIView.as_view())
]
