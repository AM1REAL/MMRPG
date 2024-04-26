from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Category(models.Model):
    name = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=64, unique=True, default="default")
    post_text = models.TextField(max_length=512)
    creation_date = models.DateTimeField(auto_now_add=True)

    category = models.ManyToManyField(Category, through="PostCategory")

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Response(models.Model):
    response_text = models.TextField(max_length=256)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    resp_date = models.DateTimeField(auto_now_add=True)
    acception = models.BooleanField(default=False)

