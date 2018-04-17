from django.conf.urls import url, include

# router = routers.DefaultRouter()
# router.register(r'companies', views.CompanyViewSet)
# router.register(r'tags', views.TagsViewSet)
# router.register(r'logos', views.LogoViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'types', views.TypeViewSet)
#
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    url(r'^', include('companyPointer.urls')),
    url(r'^', include('user.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]