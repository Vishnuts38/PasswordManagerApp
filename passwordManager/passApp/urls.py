from django.urls import path
from .views import UserSignupView,passwordCreate, rudPassword, passwordShareCreate, organisationCreate

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('create_pass/',passwordCreate.as_view(),),
    path('rud_pass/<pk>/',rudPassword.as_view(),),
    path('lc_passShare/',passwordShareCreate.as_view(),),
    path('lc_orgCreate/',organisationCreate.as_view(),)
    
]
