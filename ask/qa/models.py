# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


# class QuestionManager - менеджер модели Question

# new - метод возвращающий последние добавленные вопросы
# popular - метод возвращающий вопросы отсортированные по рейтингу
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')


# class Question - вопрос

# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField(default=0)
    
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='question_liked')
    
    objects = QuestionManager()


# class Answer - ответ

# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)













