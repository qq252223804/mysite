from django.db import models

class Question(models.Model):
    '''
    Question包含一个问题和一个发布日期
    '''

    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    '''
    Choice包含两个字段：该选项的文本描述和该选项的投票数。
    每一条Choice都关联到一个Question
    '''
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # 当然就会有可选参数，比如在votes里我们将其默认值设为0.
    votes = models.IntegerField(default=0)