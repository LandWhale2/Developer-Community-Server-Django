from django.db import models

# Create your models here.


# 글 전용 모델들

class Posts(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    content = models.TextField()

    class Meta:
        abstract = True


class Talk(Posts):
    title = "Talk"

class Projects(Posts):
    title = "Projects"

class Algorithm(Posts):
    title = "Algorithm"

class Skilltalk(Posts):
    title = "Skilltalk"