from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = RichTextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    