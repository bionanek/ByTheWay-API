from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    startdate = models.DateTimeField(auto_now_add=True)
    enddate = models.DateTimeField(null=True, default=None, blank=True)
    member_a = models.ForeignKey(User, related_name="member_a", on_delete=models.CASCADE)
    member_b = models.ForeignKey(User, related_name="member_b", on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.startdate}) : {self.member_a} & {self.member_b}"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    chat = models.ForeignKey(Chat, related_name="chat", on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)