from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from user.models import Profile, Picture


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ("created", "owner", "datafile")


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    profile_pic = PictureSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'profile_pic', 'birthdate', 'created', 'related_company',
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

        profile_pic_data = validated_data.pop('profile_pic')
        profile_pic = Picture.objects.create(**profile_pic_data)

        profile = Profile.objects.create(profile_pic=profile_pic, **validated_data)
        for interest in interests:
            profile.interests.add(interest)
        for fav in favourites:
            profile.favourites.add(fav)

        return profile



