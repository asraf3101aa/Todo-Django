from django.shortcuts import render,redirect
from .models import Todo
from django.views.generic import CreateView,ListView, DeleteView, TemplateView, DetailView, UpdateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class AddTask(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'index.html'
    success_url = '/'

class ListTask(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todos'
    ordering = ['-id']
    extra_context = {'desc': False}

class DeleteTodo(DeleteView):
    model = Todo
    success_url = ('/todos')

    
    #skip confirm template
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
class UpdateTodo(UpdateView):
    model = Todo
    fields = ['task','description','date']
    template_name = 'index.html'
    success_url = '/'
    

    
     

class ShowTodo(DetailView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todo'
    extra_context = {'desc': True}
    
     

'''

def index(request):
    return render(request, "index.html")

def addtodo(request):
    if request.method == 'POST':
        newtodo = request.POST['task']
        date = request.POST['date']
        description = request.POST['description']
        todo = Todo(task= newtodo, date = date, description = description)
        todo.save()
    #if request.method == 'POST' and (request.POST['todoid'])!='':     
        #updateTodo(request, int(request.POST['todoid']))
    return redirect('/')
        
def update(request, todoid):
    if request.method == 'POST':
    newtodo = request.POST['task']
    date = request.POST['date']
    description = request.POST['description']
    todoFromId = Todo.objects.get(id = todoid)
    todoFromId.task = newtodo
    todoFromId.date = date
    todoFromId.description = description
    todoFromId.save()
    
def delete(request, id):
    todoFromId = Todo.objects.get(id = id)
    todoFromId.delete()
    
    #return redirect('/')

def checkTodo(request, id):
    todoFromId = Todo.objects.get(id = id)
    todoFromId.is_complete = True
    todoFromId.save()
    return redirect('/')



def uncheckTodo(request, id):
    todoFromId = Todo.objects.get(id = id)
    todoFromId.is_complete = False
    todoFromId.save()
    return redirect('/')

def todos(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, "index.html", {'todos': todos},{'desc':True})






# form = TodoForm(instance=todos)
#     context = {'form': form}
#     return render(request, "tmp.html", context)
'''