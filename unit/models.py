from django.db import models


class Unit (models.Model ) : 

    university_name = models.CharField(max_length = 256 )
    unit_name = models.CharField(max_length = 256)
    group_number = models.IntegerField()
    unit_number = models.IntegerField()
    teacher = models.CharField(max_length = 256) 
    start_time = models.TimeField()
    finish_time = models.TimeField()
    first_session = models.DateField()
    second_session = models.DateField()

    