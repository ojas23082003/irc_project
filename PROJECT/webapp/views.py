from django.shortcuts import render
from django.contrib.auth.models import User, auth
import razorpay
from ircone.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def home(request):
 return render(request, 'home.html')

def product_detail(request):
 return render(request, 'productdetail.html')

def add_to_cart(request):
    if request.user.is_authenticated:
        data = { "amount": 57000, "currency": "INR", "payment_capture":1 }
        payment_order = client.order.create(data=data)
        payment_order_id = payment_order['id']
        context = {
            'amount':570,
            'api_key':RAZORPAY_API_KEY,
            'order_id':payment_order_id,
            'add' : True,
        }
        return render(request, 'addtocart.html', context)
    else:
        return render(request, 'login.html')

def buy_now(request):
 return render(request, 'buynow.html')

def profile(request):
 return render(request, 'profile.html')

def address(request):
 return render(request, 'address.html')

def orders(request):
 return render(request, 'orders.html')

def change_password(request):
 return render(request, 'changepassword.html')

def mobile(request):
 return render(request, 'mobile.html')

def login(request):
 return render(request, 'login.html')

def customerregistration(request):
 return render(request, 'customerregistration.html')

def checkout(request):
 return render(request, 'checkout.html')

def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

def remove(request):
 add = False
 return render(request, 'addtocart.html', {'add':add})

def register(request):
    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    user = User.objects.create_user(email=email, password=password, username=username,first_name=first_name,last_name=last_name)
    user.save();
    return render(request, 'login.html')

def abc(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        return render(request,'home.html')
    else:
        return render(request,'login.html',{'msg':"Invalid username or password! Please try again"})
