from django.urls import path
from .views import *

urlpatterns = [
    path('login/', HelloView.as_view(), name='login'),
    path('signup/', HelloView.as_view(), name='signup'),
]