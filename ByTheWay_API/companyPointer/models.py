from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField()
    logo = models.ForeignKey(LogoUpload, related_name="company_logo", on_delete=models.CASCADE)
    pos_lat = models.FloatField()
    pos_lon = models.FloatField()
    tags = models.ForeignKey(Tag, related_name="company_tag", on_delete=models.CASCADE)
    type = models.ForeignKey(CompanyType, related_name="company_type", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=20)


class CompanyType(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)


class LogoUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, to_field='id')
    datafile = models.FileField()
