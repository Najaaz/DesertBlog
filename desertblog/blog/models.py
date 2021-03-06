from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    image = models.ImageField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



class Comments(models.Model):
    post_connection = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"({self.post_connection}) =>{self.name}"

    class Meta:
        verbose_name_plural = "Comments"