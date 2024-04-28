from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100, blank=True, null=True)
    gender  = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    national_number = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name