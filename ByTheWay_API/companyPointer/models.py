from django.contrib.auth.models import User
from django.db import models


class LogoUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    datafile = models.FileField()


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CompanyType(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField()
    logo = models.ForeignKey(LogoUpload, related_name="company_logo", blank=True, default=None, null=True, on_delete=models.CASCADE)
    pos_lat = models.FloatField(default=10.0)
    pos_lon = models.FloatField(default=10.0)
    tags = models.ManyToManyField(Tag, related_name="company_tags")
    type = models.ForeignKey(CompanyType, related_name="company_type", to_field="id", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
