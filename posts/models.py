from django.db import models
from users.models import User
# Create your models here.




# 글 전용 모델들

class Posts(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    content = models.CharField(max_length = 255, null = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null = True)
    writer =  models.CharField(max_length = 255, null = True)
    image = models.ImageField(null= True, blank = True)

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


#댓글 모델

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    content = models.CharField(max_length = 255, null = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null = True)
    writer =  models.CharField(max_length = 255, null = True)
    
    class Meta:
        abstract = True
        ordering = ['-id']

class TalkComment(Comment):
    title = "talk"
    post = models.ForeignKey(Talk, on_delete= models.CASCADE, null = True)

class ProjectsComment(Comment):
    title = "projects"
    post = models.ForeignKey(Projects, on_delete= models.CASCADE, null = True)

class AlgorithmComment(Comment):
    title = "Algorithm"
    post = models.ForeignKey(Algorithm, on_delete= models.CASCADE, null = True)

class SkilltalkComment(Comment):
    title = "Skilltalk"
    post = models.ForeignKey(Skilltalk, on_delete= models.CASCADE, null = True)