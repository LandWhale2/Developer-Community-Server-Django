from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
# Create your models here.


class User(models.Model):
    class Meta:
        db_table = "users"
    
    created_at = models.DateTimeField(default = timezone.now)
    updated_ay = models.DateTimeField(auto_now= True)
    email = models.CharField(max_length = 128, unique= True)
    password = models.CharField(max_length = 255)
    active = models.BooleanField(default=False)
    token = models.CharField(max_length= 255, null = True)
    nickname = models.CharField(max_length = 255, null = True)
    # skills = models.CharField(max_length = 255, null = True)
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)
