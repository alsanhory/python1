from django.shortcuts import render
from django.http import HttpResponse
from noran.models import Student
# Create your views here.
def haja(request,s):
    s= Student.objects.get(id=s)
    return render(request,'bta3.html',{'studentname': s.student_name, 'studentage':s.student_age})
    
def tilal(request,sname):
    return render(request,'bta3.html',{'sname':sname,'motgayertani':9})