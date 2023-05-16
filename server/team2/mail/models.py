from django.db import models

# Create your models here.

class Mail(models.Model):
    ThreadId = models.CharField(max_length=100, primary_key=True) # メールスレッドid
    ExpiryTime = models.DateTimeField() # 締め切り日時