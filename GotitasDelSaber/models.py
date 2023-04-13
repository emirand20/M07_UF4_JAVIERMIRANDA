from django.db import models

class ClaseA(models.Model):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=9, null=True)
    
    def __str__(self):
        return self.name
    