from django.db import models
from django.utils import timezone

class Post(models.Model):

    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    pub_date = models.DateTimeField(blank=True,null=True)
    def approved_comments(self):
        return self.comments.filter(approved=True)
    def publish(self):
        self.pub_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title
class Comment(models.Model):
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    approved=models.BooleanField(default=False)

    def approve(self):
        self.approved=True
        self.save()
    
    def __str__(self):
        return self.text



# Create your models here.
