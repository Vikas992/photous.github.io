from django.shortcuts import render,HttpResponse
from datetime import date, datetime


# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        desc = request.POST.get('desc')
        contact = contact(name=name, Email=Email, Phone=Phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")    
