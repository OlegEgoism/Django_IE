from django.urls import path
from .views import info, add_info

urlpatterns = [
    path('', add_info, name='add_info'),
    path('info/', info, name='info'),
]
