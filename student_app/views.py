from django.shortcuts import render, redirect
from .forms import StudentsForm
from .models import Students

# Create your views here.

def std(request):
    if request.method =="POST":
        form = StudentsForm(request.POST)
        sid=request.POST.get('sid')
        name=request.POST.get('name')
        birth_date=request.POST.get('birth_date')
        join_date=request.POST.get('join_date')
        
        # If student exist already it will get deleted
        students = Students.objects.get(sid=sid)
        students.delete()
        # And get saved latest values
        s_info=Students(sid=sid, name=name, birth_date=birth_date, join_date=join_date)
        s_info.save()
        return redirect('/show')

    else:
        form=StudentsForm()
    return render(request, 'index.html')

def show(request):
        students =Students.objects.all()
        return render(request, 'show.html', {'students': students})

def delete(request, sid):
    students = Students.objects.get(sid=sid)
    students.delete()
    return redirect('/show')

def update(request, sid):
    
    students=Students.objects.get(sid=sid)
    return render(request, 'update.html', {'students':students})
