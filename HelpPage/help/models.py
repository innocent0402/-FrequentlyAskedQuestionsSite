from django.db import models

class QuestionType(models.Model):
    questionType = models.CharField(max_length=10)

class Question(models.Model):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
