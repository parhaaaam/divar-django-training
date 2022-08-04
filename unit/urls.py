
from . import views 
from django.urls import path 

urlpatterns = [

    path('' , views.UnitList.as_view() , name = 'unit-index') ,
    path('new' , views.NewUnit.as_view() , name = 'unit-new') ,

]