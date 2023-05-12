from django.urls import path
from .views import IndexView,AddTask,DeleteTodo,ListTask,ShowTodo,UpdateTodo
urlpatterns=[
    # path('', views.index, name='index'),
    # path('todo', views.addtodo, name='addtodo'),
    # path('todos', views.todos,name="todos"),
    # path('todo/<int:id>' ,views.update),
    # #path('todo/<int:id>' ,views.todo),
    # path('todo/<int:id>' ,views.delete),
    # #path('notdone/<int:id>' ,views.uncheckTodo)



    path('', IndexView.as_view(), name='index'),
    path('todo', AddTask.as_view()),
    path('todos', ListTask.as_view(),name='todos'),
    path('todo/<pk>/delete', DeleteTodo.as_view()),
    path('todo/<pk>/update', UpdateTodo.as_view()),
    path('todo/<pk>/update/<is_complete>', UpdateTodo.as_view()),
    path('todo/<pk>', ShowTodo.as_view()),
    #path('todo/<int:id>', UpdateTodo()),



]