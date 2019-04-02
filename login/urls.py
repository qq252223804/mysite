from django.conf.urls import url

from login import views0
app_name='login'
urlpatterns = [
    url(r'^$', views0.login,name='login'),
    url(r'^logout/$',views0.logout,name="logout"),
    # url(r'.*?', views0.login,name='login'),
# ex: /login/abc123!   /login/ 为mysite已填好的前缀
    url(r'^index/$',views0.index,name="index"),
# ex: /login/index   /login/ 为mysite已填好的前缀
    url(r'^json1/$',views0.json1,name='json1'),
    url(r'^json2/$', views0.json2, name='json2'),
    url(r'^table/$', views0.table, name='table'),


]