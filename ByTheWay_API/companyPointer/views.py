from django.contrib.auth.models import Group, User
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from companyPointer.models import Company, Tag, LogoUpload, CompanyType
from companyPointer.serializers import CompanySerializer, TagSerializer, LogoUploadSerializer, CompanyTypeSerializer


class CompanyList(APIView):
    """
        List all companies or create a new one.
    """
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetails(APIView):
    """
        Retrieve, update or delete a company instance.
    """
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
