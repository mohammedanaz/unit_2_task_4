from django.shortcuts import render, redirect
from .models import Products, UserRegister
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password



def signup(request):
    if 'username' in request.session:
        user_name = request.session['username']
        user_check = UserRegister.objects.filter(username = user_name).first()
        if user_check is not None:
            return redirect('home')
        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            if UserRegister.objects.filter(username=user_name).exists():
                form = RegisterForm()
                msg = 'User already exists'
                return render(request, 'signup.html', {'form': form, 'msg_signup': msg})
            else:
                form.save()
                return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})



def user_login(request):
    if 'username' in request.session:
        user_name = request.session['username']
        user_check = UserRegister.objects.filter(username = user_name).first()
        if user_check is not None:
            return redirect('home')
        
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=user_name, password=password) # this method returns None always?
        print('Authentication attempt for:', user_name, 'Returned user is:', user)

        user_check = UserRegister.objects.filter(username=user_name).first() # alternative method used

        if user_check is not None:
            if check_password(password, user_check.password):
                request.session['username'] = user_name
                return redirect('home')
            else:
                msg = 'Invalid'
                return render(request, 'login.html', {'msg_pass': msg})
        else:
            msg = 'does not exist'
            return render(request, 'login.html', {'msg_user': msg})
    
    return render(request, 'login.html')


def home(request):
    context = {
        'fruit' : Products.objects.order_by('prod_name')
    }
    if 'username' in request.session:
        user_name = request.session['username']
        user_check = UserRegister.objects.filter(username = user_name).first()
        if user_check is not None:
            return render(request, 'home.html', context)
    
    return redirect(user_login)



def user_logout(request):
    if 'username' in request.session:
        request.session.clear()
    return redirect('login')
