from debug_toolbar.toolbar import debug_toolbar_urls

from django.contrib import admin
from django.urls import path, include

from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/groups/', include('apps.groups.urls')),
    path('api/v1/attendances/', include('apps.attendances.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + debug_toolbar_urls()
