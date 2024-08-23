from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeForm

def index(request):
    trainees = Trainee.get_all_trainees()
    return render(request, 'trainee/index.html', {'trainees': trainees})

def create_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            trainee = form.save(commit=False)
            trainee.save_trainee()  
            return redirect('index')
    else:
        form = TraineeForm()
    return render(request, 'trainee/create_trainee.html', {'form': form})

def detail(request, id):
    trainee = Trainee.get_trainee_by_id(id)  
    return render(request, 'trainee/detail.html', {'trainee': trainee})

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()  
            return redirect('detail', id=id)
    else:
        form = TraineeForm(instance=trainee)
    return render(request, 'trainee/update_trainee.html', {'form': form})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        trainee.delete_trainee()  
        return redirect('index')
    return render(request, 'trainee/delete_trainee.html', {'trainee': trainee})
