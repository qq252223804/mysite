from django.conf.urls import url
from django.contrib import admin


from polls import views
app_name='polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
# ex: /polls/5
# 而?P<question_id>则表示我要给这个捕获的值指定一个特殊的变量名，在视图中可以通过question_id这个变量名随意的引用它，形成一个关键字参数，不用考虑参数的位置。
# 至于[0-9]+则是一个很简单的原生正则表达式，用于匹配一系列连续的数字，它匹配到的值也就是具体要传递的参数值。
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
# ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results,name='results'),
# ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote,name='vote'),
    ]