from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name
       

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name
        
class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s (%s)" % (
            self.title,
            ", ".join(tag.name for tag in self.tags.all()),
        )

class Comment(models.Model):
    user = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    def __str__(self):
        return self.user,self.body, self.email


# Create your models here.
