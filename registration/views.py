from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['confirm']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'message2': 'Username Already Exists! Try Again!'})
            user = User.objects.create_user(username=username, email=email, first_name=first_name,
                                            last_name=last_name, password=password)

            user.save()
            return redirect('register')
        return render(request, 'register.html', {'message1': 'Passwords dont match'})

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'logout.html')
        return render(request, 'login.html', {'error': 'Invalid Credentials!'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return render(request, 'logout.html')


def signup_again(request):
    return render(request, 'register.html', {'message5': 'Logged out Successfully! Login/SignUp Again?'})