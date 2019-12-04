from django.db import models

# Create your models here.


class Talk(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    content = models.TextField()

    class Meta:
        ordering = ('created',)
    