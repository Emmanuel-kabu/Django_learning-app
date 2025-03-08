import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Chatterboxconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chats_%' % self.room_name

        # Join  room group
        await self.channel_layer.groud_add(
            self.room_group_name,
            self.channel_name

        )
        await self.accept()

    async def disconnect(self, close_code):
        """ leave group """
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        # receive message from websocket

    async def receive(self, text_data):
        text_data_Json  = self.Json.load(text_data)
        message = text_data_Json['message']


# send message to room group
    async def group_send(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            { 'type':'chat_message',
             'message':'message'
             
             }
        )

        #receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # send message to websocket
        await self.send(text_data =json.dumps({
          'message': message
        }))

    



         


        
