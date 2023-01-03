from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request,'MyApp1/child.html');

# Create your views here.
def f11(request):
    return render(request,'MyApp1/child1.html');

def demo3(request):
    return render(request,'MyApp1/demo3.html');

def thankyou(request):
    return render(request,'MyApp1/thankyou.html');



