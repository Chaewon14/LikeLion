from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=10, default='me')
    category = models.CharField(max_length=10, default='all')

      #auto_now_add : 처음 객체를 생성할 때만 데이터 값을 업뎃해준다는 뜻
      #auto_now : 처음 생성뿐만 아니라 수정할 때마다 업뎃

    def __str__(self):
        return self.title
       #__str__메소드는 models에 내장되어있음. 사용자 입맛에 맞게 타이틀을 커스터마이징 할 수 있게 함.
    