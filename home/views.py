from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import NewTodoForm, UpdateTodoForm


def home(request):
    todo = Todo.objects.all().order_by('-created')
    return render(request, 'parent/base.html', {'todo': todo})


def todo_detail(request, pk):
    detail = Todo.objects.get(id=pk)
    return render(request, 'other/detail.html', {'detail': detail})


def todo_delete(request, pk):
    Todo.objects.get(id=pk).delete()
    messages.success(request, 'تسک موردنظر شما با موفقیت حذف شد.', extra_tags='success')
    return redirect('home:home')


def todo_create(request):
    if request.method == "POST":
        form = NewTodoForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['title']
            body = cd['body']
            created = cd['created']
            Todo.objects.create(title=title, body=body, created=created)
            messages.success(request, 'تسک جدید با موفقیت ایجاد شد.', extra_tags='success')
            return redirect('home:home')
    else:
        form = NewTodoForm()
    return render(request, 'other/new_todo.html', {'form': form})


def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = UpdateTodoForm(data=request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'تسک مورد نظر شما با موفقیت تغییر یافت.', extra_tags='success')
            return redirect('home:detail', pk)
    else:
        form = UpdateTodoForm(instance=todo)
    return render(request, 'other/update_todo.html', {'form': form})
