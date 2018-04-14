from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, HyperlinkedIdentityField

from .models import LogoUpload, Tag, CompanyType, Company


class LogoUploadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LogoUpload
        fields = ("created", "owner", "datafile")


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)


class CompanyTypeSerializer(serializers.HyperlinkedModelSerializer):
    namesList = CompanyType.objects.all().values_list('id', 'name')
    name = serializers.ChoiceField(choices=namesList)

    class Meta:
        model = CompanyType
        fields = ("id", "name")


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    #tags = TagSerializer(queryset=Tag.objects.all(), many=True)
    tags = TagSerializer(many=True)

    type = CompanyTypeSerializer(read_only=False)
    logo = LogoUploadSerializer()

    class Meta:
        model = Company
        fields = ("name", "description", "logo", "pos_lat", "pos_lon", "tags", "type", "created")

    def create(self, validated_data):
        logo_data = validated_data.pop('logo')
        type_data = validated_data.pop('type')
        tags = validated_data.pop('tags')
        type = CompanyType.objects.get(pk=list(type_data.values())[0])
        logo = LogoUpload.objects.create(**logo_data)
        company = Company.objects.create(logo=logo, type=type, **validated_data)

        for tag in tags:
            company.tags.add(tag)
        return company
