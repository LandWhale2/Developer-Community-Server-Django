from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length =200)
    pub_date = models.DateTimeField('date published')
    objects = models.Manager()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default= 0)

    def __str__(self):
        return self.choice_text

#모델은 기본적으로 db.models.Model 모듈을 상속받아 정의 한다 ,,, 각테이블은 클래스로 클래스의 칼럼은 클래스의 변수로 선언된다.. 
#primary 키는 따로 생성하지않아도 자동으로 생성한다
#foreign key는 id 입력없이 클래스만 지정해주면된다 . 반드시 CASCADE 속성 지정해줄것
#__str__() 함수로 해당객체의 '스트링호출 ' 시에 각 text속성을 반환
# 또한 어플에 테이블이 새로 생성된 경우에는 해당 어플의 admin 파일에 테이블을 등록해줘야한다
