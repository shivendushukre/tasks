from django.shortcuts import render, redirect
from task2.models import details


def home(request):
    if request.method == 'POST':
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        email = request.POST['email']
        phone_no = request.POST['phone no']
        gender = request.POST['gender']

        profile = details(f_name=f_name, l_name=l_name, email=email, phone_no=phone_no, gender=gender)
        profile.save()

        return redirect('home')

    else:
        return render(request, 'page1.html')


def user(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            profile = details.objects.get(email=email)
            return render(request, 'page3.html', {'profile': profile})

        except details.DoesNotExist:
            return render(request, 'page3.html', {'message': 'Sorry no user found with this email!'})

    else:
        return render(request, 'page2.html')

