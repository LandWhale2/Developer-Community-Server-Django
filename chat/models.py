from __future__ import unicode_literals
from django.db import models
from users.models import User
from django.utils import timezone


# Create your models here.

class Message(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)
     is_read = models.BooleanField(default= False)
     def __str__(self):
           return self.message
     class Meta:
           ordering = ('-timestamp',)



# class Room(models.Model):
#       roomname = models.C
#       sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#       message = models.CharField(max_length=1200)
#       timestamp = models.DateTimeField(auto_now_add=True)
#       is_read = models.BooleanField(default= False)
#       def __str__(self):
#            return self.message
#      class Meta:
#            ordering = ('-timestamp',)


class Room(models.Model):
      name = models.TextField()
      label = models.SlugField(unique= True)

      def __str__(self):
            return self.label


class RoomMessage(models.Model):
      room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
      handle = models.TextField()
      message = models.TextField()
      timestamp = models.DateTimeField(default = timezone.now, db_index= True)

      def __str__(self):
            return '[{timestamp}] {handle}:{message}'.format(**self.as_dict())
      
      @property
      def formatted_timestamp(self):
            return self.timestamp.strftime('%b %-d %-I:%M %p')
      
      def as_dict(self):
            return {'type': 'chat.message', 'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}