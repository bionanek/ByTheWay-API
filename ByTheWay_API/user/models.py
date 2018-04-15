from django.contrib.auth.models import User
from django.db import models

from companyPointer.models import Company, Tag


class Profile(models.Model):
    user = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)
    birthdate = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    related_company = models.ForeignKey(Company, blank=True, default=None, null=True, on_delete=models.CASCADE)
    interests = models.ManyToManyField(Tag, related_name="profile_interests")
    favourites = models.ManyToManyField(Company, related_name="profile_favourites") # TODO: implement algorithm and helper app that will determine which companies are favourites
    last_latitude = models.FloatField()
    last_longitude = models.FloatField()
