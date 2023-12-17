from django.shortcuts import render, redirect
from .models import bottomlevel

# bottomlevel = []

# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         new_task = request.POST['task']
#         bottomlevel.append(new_task.strip())
#         return redirect('index')
#     return render( request, 'bottomlevel/index.html', context={'task':bottomlevel})

def index(request):
    if request.method == 'POST':
        new_task = request.POST['task'].strip()
        description1 =request.POST['description']

        bottomlevel1 = bottomlevel(task_title=new_task , task_description=description1)
      
        bottomlevel1.save()
        
        return redirect('index')
    bottomlevel1 = bottomlevel.objects.all()
    
    return render(request, 'bottomlevel/index.html', context={'task':bottomlevel1})

def deletetask(request,id):
    task = bottomlevel.objects.get(taskid=id)
    task.delete()
    return redirect('index')


def edittask(request,id):
    task = bottomlevel.objects.get(taskid=id)
    if request.POST:
        new_task = request.POST['task'].strip()
        description1 =request.POST['description']
        task.task_title = new_task
        task.task_description = description1
        task.save()
        return redirect('index') 

    return render(request,'bottomlevel/edit.html',context={'task': task})
