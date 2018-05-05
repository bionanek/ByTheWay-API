from rest_framework import generics, permissions

from chat.models import Message, Chat
from chat.serializers import MessageSerializer, ChatSerializer
from ByTheWay_API.general_permissions import IsOwnerOrReadOnly


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ChatDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def get(self, *args, **kwargs):
    #     sender_id = kwargs.get('sender', None)
    #     receiver_id = kwargs.get('receiver', None)
    #     messages = Message.objects.filter(sender_id=sender_id, receiver_id=receiver_id)
    #     serializer = MessageSerializer(messages, many=True, context={'request': self.request})
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
