# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hell0(request):
    text = """<h1>welcome to my app</h1>"""
    return HttpResponse(text)

#def hello(request):
#    return render(request, "myapp/template/hello.html", {})


#def hello(request, number):
#    text="<h1>Welcome to my app %s!</h1>"% number
#    return HttpResponse(text)
