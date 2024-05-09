from django.urls import path
from .apiViewDecorator import *
from .viewsClassbased import *

urlpatterns = [
    path('login/', HelloView.as_view(), name='login'),
    path('signup/', all_data, name='signup'),
    path('dashboard/', hello_world, name='dashboard'),
    path('create-student/', CreateStudent, name='create-student'),
    path('all-student/', all_data, name='all-student'),
    path('update-student/<id>', updateStudent, name='update-student'),
    path('delete-student/<id>', deleteStudent, name='delete-student'),
    path('student/', StudentAPI.as_view(), name='retrive all students'),

]
