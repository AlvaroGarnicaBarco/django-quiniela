from django.contrib import admin
from django.urls import path, re_path, include

from apps.users.views import Login

from rest_framework import permissions

# noinspection PyUnresolvedReferences
from drf_yasg.views import get_schema_view
# noinspection PyUnresolvedReferences
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación API MiQuiniela",
      default_version='v0.1',
      description="Documentación pública de API quiniela",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alvarogarnica1997@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('api/', include('apps.users.api.urls')),
    path('api/', include('apps.quiniela_main.api.urls')),
]
