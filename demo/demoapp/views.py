from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from . models import Demotravel
# Create your views here.
def home(request):
    obj=Demotravel.objects.all()
    return render(request, "index.html", {'result': obj})



#def about(request):
 #   return HttpResponse("This page is contains details about this project")
#def contact(request):
 #   return render(request,"contact.html")
#def details(request):
 #   return HttpResponse(" This is a demo project and its details")
#def thanks(request):
 #   return render(request,"thanks.html")

#def calculations(request):
 #   x=int(request.GET['num1'])
  #  y= int(request.GET['num2'])
   #s=x-y
    #m=x*y
    #d=x/y
    #return render(request,"calculations.html",{'add':a,'sub':s,'mul':m,'div':d})