from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.


def index(requests):
    todo = Todo.objects.all()
    if requests.method == 'POST':
        new_todo = Todo(
            title=requests.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(requests, "index.html", {'todos': todo})


def delete(requests, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
