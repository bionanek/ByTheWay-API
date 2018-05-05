from django.conf.urls import url

from chat import views

urlpatterns = [
    #url(r'^messages/(?P<sender>[0-9]+)/(?P<receiver>[0-9]+)/$', views.MessageList.as_view(), name='message-list'),
    url(r'^messages/$', views.MessageList.as_view(), name='message-list'),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.MessageDetails.as_view(), name='message-detail'),
    url(r'^chat/$', views.ChatList.as_view(), name='chat-list'),
    url(r'^chat/(?P<pk>[0-9]+)/$', views.ChatDetails.as_view(), name='chat-detail')
]