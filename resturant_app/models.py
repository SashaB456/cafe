from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)