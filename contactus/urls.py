
from . import views 
from django.urls import path 

urlpatterns = [

    path('' , views.Contact.as_view() , name = 'index') ,
    path('success/' , views.Success.as_view() , name = 'index') ,

]