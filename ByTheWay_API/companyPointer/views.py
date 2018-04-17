from rest_framework import generics, permissions

from companyPointer.models import Company, Tag, LogoUpload, CompanyType
from companyPointer.permissions import IsOwnerOrReadOnly
from companyPointer.serializers import CompanySerializer, TagSerializer, LogoUploadSerializer, CompanyTypeSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CompanyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)


class TagsList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TypeList(generics.ListCreateAPIView):
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeSerializer


class TypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeSerializer


class LogoList(generics.ListCreateAPIView):
    queryset = LogoUpload.objects.all()
    serializer_class = LogoUploadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LogoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = LogoUpload.objects.all()
    serializer_class = LogoUploadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
