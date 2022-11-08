from django.db import models
from datetime import datetime

class List(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth_date = models.DateField(default=datetime.now)
