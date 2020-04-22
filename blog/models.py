from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE) ##Linking author with the user we create for application
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):##This is using to tell django where to go after creating post
        return reverse('post_details',kwargs={'pk':self.pk})

class Comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)      ##'approved_comment' it should match with
                                                               # return self.comments.filter(approved_comment=True)
    def __str__(self):
        return self.author

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):##This is using to tell django where to go after adding a comment
        return reverse('post_list')
    