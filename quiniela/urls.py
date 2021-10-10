from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-users/', include('apps.users.api.urls')),
    path('api-quinielamain/', include('apps.quiniela_main.api.urls')),
]
