from django.db import models
# Create your models here.


class User(models.Model):
    class Meta:
        db_table = "users"
    
    created_at = models.DateTimeField(auto_now_add= True)
    updated_ay = models.DateTimeField(auto_now= True)
    email = models.CharField(max_length = 128, unique= True)
    password = models.CharField(max_length = 255)
    active = models.BooleanField(default=False)