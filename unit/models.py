from calendar import WEDNESDAY
from django.db import models


class Unit (models.Model ) : 

    SATURDAY = '0'
    SUNDAY = '1'
    MONDAY = '2'
    TUESDAY = '3'
    WEDNESDAY = '4'
    DAYS_OF_WEEK = (
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
    )

    department = models.CharField(max_length = 256 )
    name = models.CharField(max_length = 256)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length = 256) 
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.CharField(max_length=10, choices=DAYS_OF_WEEK, default=SATURDAY)
    second_day = models.CharField(max_length=10, choices=DAYS_OF_WEEK, default=SATURDAY)

    