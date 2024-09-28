from django.shortcuts import render

# Create your views here.

def todolist(request):
    todos=Todo.objects.all()
    print(todos)
    return render(request,"todo/todolist.html",{"todos":todos})
