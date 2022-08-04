
from . import views 
from django.urls import path 

urlpatterns = [

    path('' , views.UnitList.as_view() , name = 'index') ,
]