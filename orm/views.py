from multiprocessing import context
from django.shortcuts import render
from .models import Student
# Create your views here.

def studentData(request):
    
    students = Student.objects.all().values()
    print(students[0].get('id'))
    print(students[0])
    studentlist = []
    for i in students[0].values():
        studentlist.append(i)
    
    print("student list",studentlist)


    context = {
        'students':studentlist
    }
    return render(request,'orm/student.html',context)
