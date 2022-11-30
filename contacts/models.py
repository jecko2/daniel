from django.db import models
from article.models import Post
from django_editorjs import EditorJsField


# Create your models here.


class Subscription(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
    
    def __str__(self):
        return f"{self.email}"
    
    


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    is_responded = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        
        
    def __str__(self):
        return f"{self.name} on {self.pub_date.day}/{self.pub_date.month}"
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    comment = models.TextField()
    is_valid = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    