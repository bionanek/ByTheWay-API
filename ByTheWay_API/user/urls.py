from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from user import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view(), name='user-detail'),
    url(r'^profiles/$', views.ProfilesList.as_view(), name='profile-list'),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.ProfileDetails.as_view(), name='profile-detail'),
    url(r'^pictures/$', views.PicturesList.as_view(), name="profile-pic-list"),
    url(r'^pictures/(?P<pk>[0-9]+)/$', views.PictureDetails.as_view(), name="profile-pic-details")
]

urlpatterns = format_suffix_patterns(urlpatterns)