from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout



# Create your views here.


def signUp(request):

    if request.method =='POST':

        #username= request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']

        email = request.POST['email']

        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        user = User.objects.create_user(username, email, pass1)

        user.first_name = fname
        user.last_name = lname

        user.save()

        messages.success(request, 'your account has been succesfully created')
        return redirect('signin')



    return render(request, 'home/signup.html')


def signIn(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username= username , password = password)
        
        if user is not None:
            login(request, user)

            fname = user.first_name
            return redirect('home')
        
        else:
            messages.error(request, 'user or password does not correct')
            return redirect('home')
        
    return render(request, 'home/signin.html')

def signOut(request):

    pass






def home(request):

    return render(request, 'home/home.html')
