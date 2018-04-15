from rest_framework import generics

from companyPointer.models import Company, Tag, LogoUpload, CompanyType
from companyPointer.serializers import CompanySerializer, TagSerializer, LogoUploadSerializer, CompanyTypeSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


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


class LogoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = LogoUpload.objects.all()
    serializer_class = LogoUploadSerializer
