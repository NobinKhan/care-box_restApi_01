from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(verbose_name="Author", max_length=100, blank=True, null=True)
    title = models.CharField(verbose_name="Title", max_length=250, blank=True, null=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"