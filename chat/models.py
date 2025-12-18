from django.db import models
from user.models import NewRequest

# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def delete_old_messages():
        # Determine the number of messages to keep
        max_messages = 15
        messages_to_delete = Message.objects.count() - max_messages

        if messages_to_delete > 0:
            # Identify the messages to delete based on the retention policy
            messages = Message.objects.order_by('timestamp')[:messages_to_delete]

            # Delete the identified messages
            for message in messages:
                message.delete()

class PrivateMessage(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    request=models.ForeignKey(NewRequest, on_delete=models.CASCADE)

    @staticmethod
    def delete_old_messages():
        # Determine the number of messages to keep
        max_messages = 15
        messages_to_delete = PrivateMessage.objects.count() - max_messages

        if messages_to_delete > 0:
            # Identify the messages to delete based on the retention policy
            messages = PrivateMessage.objects.order_by('timestamp')[:messages_to_delete]

            # Delete the identified messages
            for message in messages:
                message.delete()