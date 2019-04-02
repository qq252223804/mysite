from django.contrib import admin

# Register your models here.
#往数据库注册表单
from .models import UserInfo

admin.site.register(UserInfo)

