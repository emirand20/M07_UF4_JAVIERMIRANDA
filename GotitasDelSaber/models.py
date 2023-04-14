from django.db import models

class ClaseA(models.Model):
    name = models.CharField(max_length=30, null=True)
    id = models.CharField(max_length=10, null=True)
    age = models.CharField(max_length=3, null=True)
    birthplace = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=10, null=True)
    gendre = models.CharField(max_length=10, null=True)
    bio = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return self.name
    