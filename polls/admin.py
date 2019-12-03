from django.contrib import admin
from polls.models import Question, Choice #테이블이 새로생성되면 admin.py 에 알려줘야한다

admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
