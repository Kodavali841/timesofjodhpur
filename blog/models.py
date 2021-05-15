from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog-home')


# class Comment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     comment_text = models.CharField(max_length=500, null=True)

#     def __str__(self):
#         return self.comment_text


# class Like(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
#     post = models.ForeignKey(Post, models.CASCADE)

#     def __str__(self):
#         return self.post.title