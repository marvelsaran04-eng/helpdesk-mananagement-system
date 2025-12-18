from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()

        # Add the new connection to a group
        self.group_name = "chat"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Load previous messages asynchronously
        previous_messages = await self.load_previous_messages()

        previous_messages.reverse()
         # Send previous messages to the user
        for message in previous_messages:
            await self.send(text_data=json.dumps(message))

    async def disconnect(self, close_code):
        # Log the close code
        print("WebSocket connection closed with code:", close_code)

        # Remove the connection from the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        # Save the received message to the database
        await self.save_message(username, message)


        # Broadcast message to all connected users in the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'username': event['username'],
            'message': event['message']
        }))

    @sync_to_async
    def save_message(self, username, message):
        from .models import Message
         # Delete old messages if the limit is exceeded
        Message.delete_old_messages()
        message = Message.objects.create(username=username, content=message)

    @sync_to_async
    def load_previous_messages(self):
        from .models import Message
        messages = Message.objects.order_by('-timestamp')[:10]

        # Collect previous messages
        previous_messages = []
        for message in messages:
            previous_messages.append({
                'username': message.username,
                'message': message.content
            })
    
        return previous_messages
    


