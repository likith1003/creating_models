from django.shortcuts import render
from app.models import *
# Create your views here.
def home(request):
    d = {
        'name':"Steve",
        "age":28,
        "pay":1500
    }
    return render(request, 'home.html', d)

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        email = request.POST.get('email')
        CDO = Details(username=un, password=pw, email=email)
        CDO.save()
        return render(request, 'login.html')
    return render(request, 'register.html')