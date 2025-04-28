from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __init__(self):
        return self.name

class Thoughts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __init__(self):
        return self.title

class Comment(models.Model):
    thoughts = models.ForeignKey(Thoughts, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    author = models.CharField(max_length=100)

    def __init__(self):
        return f"Comment by {self.author}"