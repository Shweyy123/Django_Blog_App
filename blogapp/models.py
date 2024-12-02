from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)