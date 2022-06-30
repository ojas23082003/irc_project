from django.shortcuts import render
from django.contrib.auth.models import User, auth

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']

#         user = User.objects.create_user(email=email, password=password, username=username,first_name=first_name,last_name=last_name)
#         user.save();
#         return render(request, 'login.html')
#     else:
#         return render(request, 'customerregistration.html')

# def abc(request):
#     username = request.POST['username']
#     password = request.POST['password']

#     user = auth.authenticate(username=username,password=password)
#     if user is not None:
#         auth.login(request, user)
#         return render(request,'home.html')
#     else:
#         return render(request,'login.html',{'msg':"Invalid username or password! Please try again"})
