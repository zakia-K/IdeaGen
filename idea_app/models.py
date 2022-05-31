from django.db import models

class Picture(models.Model):
    picture_name = models.CharField(max_length=200)
    picture_loc = models.CharField(max_length=200)


