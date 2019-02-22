from django.db import models
from django.contrib.auth.models import User

# class Question - вопрос

# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"
class Question(models.Model):
	title = models.CharField(255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	
	author = models.OneToOneField(User)
	likes = models.ManyToManyField(User, related_name='question_liked')

# class Answer - ответ

# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	
	question = models.ForeignKey(Question)
	author = models.OneToOneField(User)


# class QuestionManager - менеджер модели Question

# new - метод возвращающий последние добавленные вопросы
# popular - метод возвращающий вопросы отсортированные по рейтингу
class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	def popular(self):
		return self.order_by('-rating')