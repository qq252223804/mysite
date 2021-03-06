from django.conf.urls import url

from login import views as view02
app_name='login'
urlpatterns = [
    url(r'^$', view02.login, name='login'),
    url(r'^admin/.*?', view02.login, name='login'),
    url(r'^logout/$', view02.logout, name="logout"),
    # url(r'.*?', views0.login,name='login'),
# ex: /login/abc123!   /login/ 为mysite已填好的前缀
    url(r'^index/$', view02.submit_login, name="submit_login"),
# ex: /login/index   /login/ 为mysite已填好的前缀
    url(r'^json1/$', view02.json1, name='json1'),
    url(r'^json2/$', view02.json2, name='json2'),
    url(r'^table/$', view02.table, name='table'),
    url(r'^ajax/$', view02.ajax, name='ajax'),
    url(r'^demo/$', view02.demo, name='demo'),

    url(r'^submit_form/$', view02.submit_form, name='submit_form'),
    url(r'^tab/$', view02.Active_tab, name='Active_tab'),
    url(r'^user_table/$', view02.user_table, name='user_table'),
]