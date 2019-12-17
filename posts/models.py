from django.db import models
from users.models import User
# Create your models here.




# 글 전용 모델들

class Posts(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    content = models.CharField(max_length = 255, null = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null = True)
    writer =  models.CharField(max_length = 255, null = True)

    class Meta:
        abstract = True
        ordering = ['-id']


class Talk(Posts):
    title = "talk"

class Projects(Posts):
    title = "projects"

class Algorithm(Posts):
    title = "Algorithm"

class Skilltalk(Posts):
    title = "Skilltalk"