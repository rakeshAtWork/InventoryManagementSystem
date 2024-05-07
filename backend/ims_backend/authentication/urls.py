from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HelloView.as_view(), name='home'),
]