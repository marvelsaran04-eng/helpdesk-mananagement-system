from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.contrib.auth import login as auth_login, authenticate

from agent.models import CustomUser

def startup(request):
    return render(request, "startup.html")



    

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            request.session['user_id'] = user.id
            if user.role == CustomUser.AGENT:
                return redirect('agent')
            else:
                return redirect('user')  
        else:
            
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        
        return render(request, 'login.html')

def logout_user(request):
    request.session.clear()
    logout(request)
    # Redirect to the starting web page
    return redirect("startup")

