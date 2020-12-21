from django.db import models

from django.db import models


class Table(models.Model):
    Stu_Name = models.CharField(max_length=50)
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    Maths = models.IntegerField()
    Com_Science = models.IntegerField()

    def __str__(self):
        return self.Stu_Name
