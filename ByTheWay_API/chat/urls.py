from django.conf.urls import url

from chat import views

urlpatterns = [
    url(r'^api/messages/(?P<sender>[0-9]+)/(?P<receiver>[0-9]+)/$', views.MessageList.as_view(), name='message-list'),
    # url(r'^api/messages/$', views.MessageDetails.as_view(), name='message-detail'),
]