
from django.shortcuts import render, redirect, get_object_or_404
from .models import tsk
from .forms import Taskform

from django.db.models.functions import Replace




# Create your views here.
def task_list(request):
    Data = tsk.objects.all().order_by('-id')
    return render(request,'todo/task_list.html',{'Data':Data } )




def task_new(request):
    if request.method=='POST':
        form=Taskform (request.POST)
        if form.is_valid():
             Post_data=form.save()
             return redirect(task_list)

    form=Taskform()
    return render(request,'todo/index.html',{'form':form})



def task_delete(request,pk):
    task=get_object_or_404(tsk,pk=pk)
    task.delete()
    return redirect('task_list')





def task_update(request,pk):
    task=get_object_or_404(tsk,pk=pk)
    task.status='complete'
    task.save()
    return redirect('task_list')







    


    


        
            
            
    