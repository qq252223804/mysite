
#数据存储
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user=models.CharField(max_length=32,unique=True)
    pwd=models.CharField(max_length=32)

    class meta:
        db_table = 'client'