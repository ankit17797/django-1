from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.

def hi(request):
    #template = get_template("app/index.html")
    #return HttpResponse('<h1> This is my home page</h1>')
   # return HttpResponse(template.render())
    return render(request,'app/index.html')
