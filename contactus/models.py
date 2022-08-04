from django.db import models


class Contact(models.Model) : 

    title = models.CharField(max_length = 100)
    text = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 256)

