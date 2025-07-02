from django.db import models

# 게시글
# 제목
# 내용

class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
