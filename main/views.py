from typing import Text
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
# Create your views here.
from .models import Todo

def home_view(request,*args,**kwargs):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request,'main/index.html',{"todo_items":todo_items})


def add_todo(request):
    print(request.POST)
    added_date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(added_date=added_date,text=content)
    print(Todo.objects.all())
    return redirect("/main")


def delete_todo(request,id):
    
    obj = get_object_or_404(Todo,pk=id)
    obj.delete()
    
    return redirect("/main")
    