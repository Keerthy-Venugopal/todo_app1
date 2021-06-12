from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class TaskListview(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('condetail',kwargs={'pk':self.object.id})

# class Taskdeleteview(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('condelete')


def task_view(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()

    return render(request,'task_view.html',{'obj1':obj1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{task:'task'})

def update(request,updateid):
    obj=Task.objects.get(id=updateid)
    form=TodoForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})




