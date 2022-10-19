from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
def helloView(request):
    if request.method == "GET":
        return render(request, 'hello_page.html')
    else:
        if request.POST.get('sign_in'):
            user = authenticate(request, username=request.POST['user_name'], password=request.POST['login_password'])
            if user is None:
                return render(request, 'hello_page.html', {'error': 'Username or password did not match!'})
            else:
                login(request, user)
                return redirect('mainView')

def mainView(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'app\main.html')
        else:
            pass
    else:
        return redirect('helloView')