from django.urls import path
from .views import *

urlpatterns = [
    path('login/', HelloView.as_view(), name='login'),
    path('signup/',all_data, name='signup'),
    path('dashboard/', hello_world, name='dashboard'),
    path('create-student/',CreateStudent,name = 'create-student'),
    path('all-student/',all_data, name = 'all-student'),
]