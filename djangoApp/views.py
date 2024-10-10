from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student 
# Create your views here.
@csrf_exempt



def home(request):
    student_list=Student.objects.all()
    # for student in student_list:
    #   print(student.first_name+" - "+ student.last_name + " ," + str(student.roll))

    
    context={
        
        "student_list":student_list

    }
    return render(request, 'home.html',context )

    

def request_handle(request):
    if request.method == "POST":
        #add data
        return HttpResponse("Hello this is POST response")

    if request.method == "GET":
        #data get quert 
        return HttpResponse("Hello this is GET response")

    if request.method == "PUT":
        #upadte
        return HttpResponse("Hello this is PUT response")

    if request.method == "DELETE":
        #vsdvag
        return HttpResponse("Hello this is DELETE response")
    

    context={
        
        "student_list":student_list

    }
    return render(request, 'home.html',context )


def add_student(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        roll_number= request.POST.get('roll')
        Student.objects.create(first_name=first_name,last_name=last_name,roll=roll_number)

    return redirect ('/')

def update_student(request):
    if request.method == 'POST':
        #Catch  The data
        
        student_id= request.POST.get('student_id')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        roll_number= request.POST.get('roll_no')

        Student.objects.filter(pk=student_id).update(first_name=first_name,last_name=last_name,roll=roll_number)

    return redirect ('/')


def delete_student(request):
    if request.method == 'GET':
        student_id= request.GET['student_id']

        Student.objects.filter(pk=student_id).delete()
        
      

    return redirect ('/')




