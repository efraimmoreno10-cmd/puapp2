from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('puapp:puapp_list')
    else:       
        form = TaskForm()
    # tasks = Task.objects.all()
    completed_tasks = Task.objects.filter(is_completed=True)
    incomplete_tasks = Task.objects.filter(is_completed=False)
    
    return render(request, 'task_list.html', {
        
        'form': form,
        # 'tasks': tasks
        'completed_tasks': completed_tasks,
        'incomplete_tasks': incomplete_tasks,
        
        })    
    
