from django.urls import path
from apps.users.api.views import user_list_api_view, user_detail_api_view

urlpatterns = [
    path('user/', user_list_api_view, name='user_api'),
    path('user/<int:pk>/', user_detail_api_view, name='user_detail_api')
]

