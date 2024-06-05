# core/models.py
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CompanyData(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    description = models.TextField()
    founded = models.IntegerField()
    size_range = models.CharField(max_length=50)
    employees = models.IntegerField(null=True, blank=True) 
