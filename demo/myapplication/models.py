from django.db import models
# Name: bansri shah
# course: CST8333 Programming Language Research Project.
# Assignment 4
# student-number: 040920837

# Create your models here.
class assign4(models.Model):
    REF_DATE = models.CharField(max_length=20)
    GEO = models.CharField(max_length=100)
    DGUID = models.CharField(max_length=100)
    Sex = models.CharField(max_length=100)
    Agegroup = models.CharField(max_length=100)
    Studentresponse = models.CharField(max_length=100)
    UOM = models.CharField(max_length=100)
    UOM_ID = models.CharField(max_length=100)
    SCALAR_FACTOR = models.CharField(max_length=100)
    SCALAR_ID = models.CharField(max_length=100)
    VECTOR = models.CharField(max_length=100)
    COORDINATE = models.CharField(max_length=100)
    VALUE = models.CharField(max_length=100)
    STATUS = models.CharField(max_length=100)
    SYMBOL = models.CharField(max_length=100)
    TERMINATED = models.CharField(max_length=100)
    DECIMALS = models.CharField(max_length=100)
    objects = models.Manager()
