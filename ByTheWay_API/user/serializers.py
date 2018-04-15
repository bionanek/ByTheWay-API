import datetime

from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField, PrimaryKeyRelatedField

from companyPointer.models import Tag, Company
from companyPointer.serializers import TagSerializer, CompanySerializer
from user.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    interests = TagSerializer(many=True, read_only=True)
    favourites = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'birthdate', 'created', 'related_company',
                  'interests', 'favourites', 'last_latitude', 'last_longitude')

    def create(self, validated_data):
        interests = validated_data.pop('interests')
        favourites = validated_data.pop('favourites')

        # interests = Tag.objects.get()
        # favourites = Company.objects.get()
        # user = User.objects.get(pk=1)
        # birthdate = datetime.datetime.now()
        # created = datetime.datetime.now()
        # related_company = None
        # last_latitude = 100.1
        # last_longitude = 100.2

        #profile = Profile.objects.create(user=user, birthdate=birthdate, created=created, related_company=related_company,
        #                                 last_latitude=last_latitude, last_longitude=last_longitude)

        profile = Profile.objects.create(**validated_data)
        for interest in interests:
            profile.interests.add(interest)
        for fav in favourites:
            profile.favourites.add(fav)

        return profile
