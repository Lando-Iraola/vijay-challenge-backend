from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    content = models.TextField(blank=False)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title