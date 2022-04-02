from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .form import TodoForm
from .models import TodoList

# Create your views here.
def home(request):
    form = TodoForm()
    tasks = TodoList.objects.filter(status=False)
    return render(request,"home.html",{
        'title':'ToDo',
        'header':'welcome',
        'form' : form,
        'tasks' : tasks,
    })

def add(request):
    form = TodoForm(request.POST)
    if(form.is_valid()):
        todo = TodoList.objects.create(task=form.cleaned_data['todo'])
        todo.save()
        return redirect('/')
    else:
        return HttpResponse("fake")


def finshed(request,pk):
    try:
        form = TodoForm()
        todo = TodoList.objects.get(id=pk)
        todo.status = True
        todo.save()

        return redirect('/')
    except Exception as e:
        return HttpResponse("Something went wrong")
        
def edit(request,pk):
    todo = TodoList.objects.get(id=pk)
    form = TodoForm(request.POST,
        initial={
            "todo" : todo.task,
        }
    )
    print("Entere1")
    if request.method == "POST":
        print("Entere2")
        if(form.is_valid()):
            print("Entere3")
            todo.task = form.cleaned_data['todo']
            todo.save()
            return redirect('/')
        else:
            print("Else update")
    return render(request,"update.html",{
        "form":form,
        "pk":pk
        })

def delete(request,pk):
   todo = TodoList.objects.get(id=pk) 
   todo.delete()
   return redirect('/')