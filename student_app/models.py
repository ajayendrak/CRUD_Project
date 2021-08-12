from django.db import models


# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=100)
    birth_date=models.DateField()
    join_date=models.DateField()

    class Meta:
        db_table="students"
