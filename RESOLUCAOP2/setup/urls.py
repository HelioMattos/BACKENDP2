from django.urls import path

from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
	path('', TodoListView.as_view(), name='todo_list'),

]