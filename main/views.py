from django.shortcuts import render, redirect
from .models import Products
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout

###################################### sign up view ##################################
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            error_msg = None
            if form.errors.get('email'):
                error_msg = form.errors['email']
            elif form.errors.get('username'):
                error_msg = form.errors['username']
            elif form.errors.get('password'):
                error_msg = form.errors['password']
            elif form.errors.get('__all__'):
                error_msg = form.errors['__all__']
            return render(request, 'signup.html', {'form': form, 'error_signup': error_msg})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


############################### login view #####################################
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password) 

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            msg = 'or password wrong'
            return render(request, 'login.html', {'msg_user': msg})
        
    return render(request, 'login.html')


####################################### home view ####################################
def home(request):
    if request.user.is_authenticated:
        visit_count = request.session.get('visit_count',0)
        visit_count += 1
        request.session['visit_count'] = visit_count
        context = {
        'fruit' : Products.objects.order_by('prod_name'),
        'visit_count': visit_count
    }
        return render(request, 'home.html', context)
    
    return redirect(user_login)


############################ logout view #############################################
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')
