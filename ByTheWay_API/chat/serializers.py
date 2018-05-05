from django.contrib.auth.models import User
from rest_framework import serializers


from chat.models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""

    #sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    chat = serializers.SlugRelatedField(many=False, slug_field='id', queryset=Chat.objects.all())

    class Meta:
        model = Message
        fields = ['url', 'id', 'sender', 'receiver', 'chat', 'message', 'timestamp']


class ChatSerializer(serializers.ModelSerializer):
    member_a = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    member_b = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = ['url', 'id', 'startdate', 'enddate', 'member_a', 'member_b']

