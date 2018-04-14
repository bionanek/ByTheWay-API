from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')