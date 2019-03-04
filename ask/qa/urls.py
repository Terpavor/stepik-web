
from django.urls import path
import qa.views as views

# path(route, view, kwargs=None, name=None)
urlpatterns = [
	path('', 					views.new_questions),
	path('login/', 				views.test),
	path('signup/', 			views.test),
	path('popular/', 			views.popular_questions),
	path('question/<int:num>/', views.question_page),
	path('ask/', 				views.test),
	path('new/', 				views.test)
]
'''
	/
	/login/
	/signup/
	/question/<123>/    # вместо <123> - произвольный ID
	/ask/
	/popular/
	/new/
'''