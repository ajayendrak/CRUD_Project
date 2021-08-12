from django.shortcuts import render, redirect

from .models import Students

# Create your views here.

def std(request):
    if request.method =="POST":
        
        id=request.POST.get('id')
        name=request.POST.get('name')
        birth_date=request.POST.get('birth_date')
        join_date=request.POST.get('join_date')
        
        s_info=Students(id=id, name=name, birth_date=birth_date, join_date=join_date)
        s_info.save()
        return redirect('/show')

    else:
        
        return render(request, 'index.html')

def show(request):
        students =Students.objects.all()
        return render(request, 'show.html', {'students': students})

def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect('/show')

def update(request, id):
    
    students=Students.objects.get(id=id)
    return render(request, 'update.html', {'students':students})
