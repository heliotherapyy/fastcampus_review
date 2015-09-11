from django.db import models
from django.conf import settings

# Create your models here.


# User 모델 확장
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    biography = models.TextField()