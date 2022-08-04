
from . import views 
from django.urls import path 

urlpatterns = [

    path('' , views.Index.as_view() , name = 'index') ,
    path('login', views.Log_in.as_view(), name="login"),
    path('register' , views.Register.as_view() , name = 'register') , 
    path('profile' , views.Profile.as_view() , name = 'profile') ,
    path('profile/update' , views.Update.as_view() , name = 'update') , 
    path('logout' , views.LogoutView.as_view() , name = 'logout') ,
]