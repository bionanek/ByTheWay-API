from django.conf.urls import url, include

from rest_framework.schemas import get_schema_view

from ByTheWay_API import views

schema_view = get_schema_view(title="ByTheWay API")

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^', include('companyPointer.urls')),
    url(r'^', include('user.urls')),
    url(r'^', include('chat.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^schema/$', schema_view)
]