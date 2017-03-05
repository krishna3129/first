# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Life, Task
# Create your views here.
def life_calender(request):
    life = Life.objects.all()
    # output = ','.join([str(event) for event in life])
    return render(request, 'life/life_calender.html', {'life': life })
def life_tasks(request , pk):
    # life = Life.objects.get(pk = pk)
    life = get_object_or_404(Life, pk=pk)
    return render(request, 'life/life_tasks.html', {'life':life})
def task_detail(request, life_pk, task_pk):
    task = get_object_or_404(Task, life_id = life_pk, pk= task_pk)
    return render(request, 'life/task_detail.html', {'task': task})
