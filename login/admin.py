from django.contrib import admin

# Register your models here.
#往数据库注册表单
from .models import *

admin.site.register(UserInfo)
admin.site.register(user_form)


