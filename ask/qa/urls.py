
from django.urls import path
import qa.views as views

# path(route, view, kwargs=None, name=None)
urlpatterns = [
	path('', 					views.test),	
	path('login/', 				views.test),
	path('signup/', 			views.test),
	path('question/<int:num>/', views.test),
	path('ask/', 				views.test),
	path('popular/', 			views.test),
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