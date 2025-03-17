from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.user.is_authenticated:  # If user is logged in
        return redirect('/')
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password2 = request.POST['password2']

        if(password == password2):
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)

                user_login = auth.authenticate(username=username, password = password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)

                return redirect('settings')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
    else: 
        return render(request, 'signup.html')

def signin(request):
    if request.user.is_authenticated:  # If user is logged in
        return redirect('/')

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
    
@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
        else:
            image = request.FILES.get('image')
        
        bio = request.POST['bio']
        location = request.POST['location']

        user_profile.profileimg = image
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()
        return redirect('settings')

    return render(request, 'settings.html', {'user_profile': user_profile})