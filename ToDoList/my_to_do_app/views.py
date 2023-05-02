from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect # HttpResponse => 단순히 인자로 받은 문자열을 사용자의 화면에 보여 주도록 하는 함수
from django.urls import reverse
from .models import *                # models앞의 .은 같은 위치라는 의미

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {"todos" : todos}
    return render(request, "my_to_do_app/index.html", content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse("index"))
    # return HttpResponse("create Todo를 할 거야! =>"+user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
    