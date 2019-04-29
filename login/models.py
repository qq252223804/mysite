
#数据存储
import hashlib

from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class UserInfo(models.Model):
    user=models.CharField(max_length=50,unique=True)
    pwd=models.CharField(max_length=50)

    def __unicode__(self):
        return self.user

    class Meta:
        db_table = 'client_UserInfo' #自定义表名

    def save(self, *args, **kwargs):
        self.pwd = hashlib.sha1((self.pwd + self.user).encode("utf8")).hexdigest()
        super(UserInfo, self).save(*args, **kwargs)


class user_form(models.Model):
    class Meta:
        db_table = 'client_user_form'

    title = models.CharField('标题', max_length=50)

    money=models.CharField('金额', max_length=50)
    password = models.CharField('密码', max_length=10)

    email = models.EmailField('邮箱', null=True)

    phone = models.CharField('电话', max_length=11, null=True)



    create_date = models.DateTimeField('创建时间', auto_now_add=True)

    update_date = models.DateTimeField('最近修改时间', auto_now=True)

    add_date = models.DateTimeField('保存日期', default=timezone.now)
    modified_date = models.DateTimeField('最后修改日期', auto_now=True)