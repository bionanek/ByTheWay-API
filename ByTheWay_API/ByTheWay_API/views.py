from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'profiles': reverse('profile-list', request=request, format=format),
        'profile_pics': reverse('profile-pic-list', request=request, format=format),
        'messages': reverse('message-list', request=request, format=format),
        'chats': reverse('chat-list', request=request, format=format),
        'companies': reverse('company-list', request=request, format=format),
        'comapany-tags': reverse('company-tags', request=request, format=format),
        'company-types': reverse('companytype-list', request=request, format=format),
        'company-logos': reverse('logoupload-list', request=request, format=format),
    })
