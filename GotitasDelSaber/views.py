from django.template import Context, loader
from django.shortcuts import render

def index(request):
    return render('Gotitas del saber')

'''def a(request):
    a = True
    context = {'a':a}
    return render(request, 'users.html', context)

def b(request):
    a = False
    context = {'a':a}
    return render(request, 'users.html', context)'''


def proff(request):
    profesor = {'name': 'Raul', 'surname': 'Rufo', 'age': '19'}
    return render(request, 'proff.html', {'name': profesor['name'], 'surname': profesor['surname'], 'age': profesor['age']})


def students(request):
    students = {'name': 'Reymon', 'surname': 'Gonzalez', 'age': '19'}
    return render(request, 'students.html', {'students' : students})
