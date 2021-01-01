from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
       'variable':"this is sent"

    }
    return render(request,'index.html',context)
def about(request):

    return render(request,'about.html')
    # HttpResponse("this is about page")
def services(request):
    return render(request,'Services.html')


    return HttpResponse("this is services page")
def contact(request):
    return HttpResponse("this is contact page")
