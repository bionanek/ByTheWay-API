from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from companyPointer import views

urlpatterns = [
    url(r'^companies/$', views.CompanyList.as_view(), name="company-list"),
    url(r'^companies/(?P<pk>[0-9]+)/$', views.CompanyDetails.as_view(), name="company-detail"),
    url(r'^tags/$', views.TagsList.as_view(), name="company-tags"),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetails.as_view(), name="tag-detail"),
    url(r'^types/$', views.TypeList.as_view(), name="companytype-list"),
    url(r'^types/(?P<pk>[0-9]+)/$', views.TypeDetails.as_view(), name="companytype-detail"),
    url(r'^logos/$', views.LogoList.as_view(), name="logoupload-list"),
    url(r'^logos/(?P<pk>[0-9]+)/$', views.LogoDetails.as_view(), name="logoupload-detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)
