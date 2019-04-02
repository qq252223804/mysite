from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question


def index(request):
    '''
    显示最新的一些问卷
    :param request:
    :return:
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# 调用 Template 对象 的 render() 方法并传递 context 来填充模板：
def detail(request,question_id):
    '''
    显示一个问卷的详细文本内容
    :param request:
    :param question_id:
    :return:
    '''
    # 如果查询的对象不存在的话，会抛出一个Http404的异常
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    '''
    显示某个问卷的投票或调查结果
    :param request:
    :param question_id:
    :return:
    '''
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    '''
    处理针对某个问卷的某个选项的投票动作
    :param request:
    :param question_id:
    :return:
    '''
    return HttpResponse("You're voting on question %s." % question_id)