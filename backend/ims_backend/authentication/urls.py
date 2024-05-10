from django.urls import path
from .apiViewDecorator import *
from .viewsClassbased import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', HelloView.as_view(), name='login'),
    path('signup/', all_data, name='signup'),
    path('dashboard/', hello_world, name='dashboard'),
    path('create-student/', CreateStudent, name='create-student'),
    path('all-student/', all_data, name='all-student'),
    path('update-student/<id>', updateStudent, name='update-student'),
    path('delete-student/<id>', deleteStudent, name='delete-student'),
    path('student/', StudentAPI.as_view(), name='retrive all students'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register-user/", RegisterUser.as_view(), name='RegisterUser'),
    path("login-user/", UserLoginView.as_view(), name='login'),
]
