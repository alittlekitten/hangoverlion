from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    board = models.ForeignKey('Board',on_delete=models.CASCADE, related_name='comments')
    comment_author = models.CharField(max_length = 10)
    comment_contents = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
