from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task1'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskdeleteView(DeleteView):
    odel = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

    def get_queryset(self):
        return Task.objects.all()


def add(request):
    task = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date','')
        tasks = Task(name=name, priority=priority ,date=date)
        tasks.save()

    return render(request, 'home.html', {'task': task})


def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update_task(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        form=TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('cbvhome')
    else:
        form = TodoForm(instance=task)
    return render(request,'update.html',{'form': form,'task':task})



