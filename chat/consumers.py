from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    # 웹소켓 연결시 실행
    def connect(self):
        #chat/routing.py 에있는 url (r'~~~~~consumers~~~)에서 room_name 을 가져옵니다
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        #그룹에 join , send 등과 같은 동기적인 함수를 비동기적으로 사용하기 위해서는 async_to_sync 로 감싸줘야한다
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        #연결 종료시 실행
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    #websocket 에게 메세지 receive
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        #room group에 메세지 send
        async_to_sync(self.channel_receive.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message' : message
            }
        )
    
    #room group 에서 메세지 receive
    def chat_message(self, event):
        message = event['message']

        #WebSocket 에 메세지 전송

        self.send(text_data=json.dumps({
            'message': message
        }))