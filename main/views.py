from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Signup
from django.core.mail import EmailMessage , send_mail
from django.conf import settings
from django.template.loader import render_to_string

def home(request):
    allusers = Signup.objects.order_by('-id')
    return render(request, 'home.html', {
        'allusers' : allusers 
    })

def oneuser(request, signup_id):
    oneuser = get_object_or_404(Signup, pk = signup_id)
    return render(request, {
		'oneuser' : oneuser,

		})


def signup(request):
    '''if request.method == 'POST':
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        signup = Signup(name=name , dob=dob , email=email , phone=phone)
        signup.save()'''

    if request.method == 'POST':
        # sign up the user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'signup.html', {'error': 'username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'], password=request.POST['password1'])
                auth.login(request, user)
                
                name=request.POST.get('name')
                dob=request.POST.get('dob')
                email=request.POST.get('email')
                phone=request.POST.get('phone')
                signup = Signup(name=name , dob=dob , email=email , phone=phone)
                signup.save()


                email1= EmailMessage(

                    'SmartRegister Confirmation',
                    'Hi! Thanks for registering at SmartRegister. This mail confirms that you have successfully registered at SmartRegister.',
                    #settings.EMAIL_HOST_USER,
                    'sarveshdevelops@gmail.com',
                    [request.POST['email']],

                )
                email1.fail_silently=False
                email1.send()




                #return render(request, 'ebook/home.html', {'success': 'You are successfully registered and logged in!'})
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Passwords not matched!'})
    else:
        # user wants to sign up
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        # login user
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            #return render(request, 'ebook/home.html', {'success': 'You are successfully logged in!'})
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Incorrect email and password'})
    else:
        # user wants to login
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')
