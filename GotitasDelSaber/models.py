from django.db import models

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    birthplace = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    bio = models.TextField()