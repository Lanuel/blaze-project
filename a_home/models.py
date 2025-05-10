from django.db import models
import uuid


class Post(models.Model):
    artist = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    body = models.TextField()
    cover_image = models.ImageField(upload_to='cover_images/', null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']


class Icon(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='icon_images/')

    def __str__(self):
        return self.title