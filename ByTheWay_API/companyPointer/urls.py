from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from companyPointer import views

urlpatterns = [
    url(r'^companies/$', views.CompanyList.as_view()),
    url(r'^companies/(?P<pk>[0-9]+)/$', views.CompanyDetails.as_view()),
    url(r'^tags/$', views.TagsList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
