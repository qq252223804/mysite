
#数据存储
import hashlib

from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class UserInfo(models.Model):
    user=models.CharField(max_length=50,unique=True)
    pwd=models.CharField(max_length=50)

    #默认返回
    def __str__(self):
        return self.user
    class Meta:
        db_table = 'client_UserInfo' #自定义表名

    def save(self, *args, **kwargs):
        self.pwd = hashlib.sha1(self.pwd.encode("utf8")).hexdigest()
        super(UserInfo, self).save(*args, **kwargs)



class user_form(models.Model):

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'client_user_form'

    orderno=models.CharField('表单id', max_length=50)
    title = models.CharField('标题', max_length=50)
    phone = models.CharField('电话', max_length=11)
    # DecimalField(max_digits='数字允许的最大位数', decimal_places='小数的最大位数')：十进制浮点数
    money=models.DecimalField ('金额', max_digits=10,decimal_places=2)
    password = models.CharField('密码', max_length=50)
    email = models.EmailField('邮箱', null=True)
    city=models.CharField('城市', max_length=50)
    hobbies=models.CharField('爱好', max_length=50,null=True)
    off_on=models.BooleanField('开关',default=True)
    #状态为0，1,2 对应'刚创建'，'开发中'，'已提测'
    status=models.IntegerField('状态',default=0)
    # 0代表男  1代表女
    sex=models.IntegerField('性别' ,default=0)
    content=models.CharField('文本描述',max_length=150)
    add_date = models.DateTimeField('保存日期', default=timezone.now)
    search_time=models.DateTimeField('按范围搜索日期', auto_now=True,null=True)
    search_times = models.DateTimeField('按范围搜索日期', auto_now=True,null=True)