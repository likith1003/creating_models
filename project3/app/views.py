from django.shortcuts import render, HttpResponse
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
    if request.method == 'POST':
        users = Details.objects.all()
        un = request.POST.get('username')
        pw = request.POST.get('password')
        for user in users:
            if user.username == un:
                if user.password == pw:
                    d = {'user':user}
                    return render(request, 'home.html', d)
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('Invalid Username')
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