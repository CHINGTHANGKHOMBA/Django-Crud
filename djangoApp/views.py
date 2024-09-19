from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt

def home(request):
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
    

def request_handle(request):
    print(request.method)

    return HttpResponse("response", status=200 )


