from rest_framework import generics
from rest_framework.response import Response

from chat.models import Message
from chat.serializers import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
   # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, *args, **kwargs):
        sender_id = kwargs.get('sender', None)
        receiver_id = kwargs.get('receiver', None)
        messages = Message.objects.filter(sender_id=sender_id, receiver_id=receiver_id)
        serializer = MessageSerializer(messages, many=True, context={'request': self.request})
        return Response(serializer.data)


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)