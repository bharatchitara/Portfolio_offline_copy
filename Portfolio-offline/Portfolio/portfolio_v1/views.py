from django.shortcuts import render


# Create your views here.


def base(request):
    return render(request, 'index.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request, "contact.html")
     
### for testing

def test(request):
    return render (request, 'test.html')     


