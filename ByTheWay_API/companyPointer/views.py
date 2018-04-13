from django.contrib.auth.models import Group, User
from django.shortcuts import render
from rest_framework import viewsets

from companyPointer.models import Company, Tag, LogoUpload, CompanyType
from companyPointer.serializers import CompanySerializer, TagSerializer, LogoUploadSerializer, UserSerializer, \
    GroupSerializers, CompanyTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Api Endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class CompanyViewSet(viewsets.ModelViewSet):
    """
        Api Endpoint that allows company to be viewed or edited
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TagsViewSet(viewsets.ModelViewSet):
    """
        Api endpoint that allows tags to be viewed or edited
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """
        Api endpoint that allows tags to be viewed or edited
    """
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeSerializer


class LogoViewSet(viewsets.ModelViewSet):
    """
        Api endpoint that allows logos to be viewed or edited
    """
    queryset = LogoUpload.objects.all()
    serializer_class = LogoUploadSerializer
