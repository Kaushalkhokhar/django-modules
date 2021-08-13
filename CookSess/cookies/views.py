from datetime import datetime, timedelta
from django.shortcuts import render

def set(request):
    response = render(request, 'cookies/home.html')
    # response.set_cookie('user', 'kush')
    # response.set_cookie('user', 'kush', max_age=60) # espires in 60 second
    response.set_cookie('user', 'kush', expires=datetime.utcnow()+timedelta(days=2)) # espires in 2 days
    response.set_signed_cookie('user', 'kush', salt='kush',  
            expires=datetime.utcnow()+timedelta(days=2)) # signed cookies uses salt to create and get it
    return response

def get(request):
    # c = request.COOKIES.get('user')
    c = request.get_signed_cookie('user', salt='kush')
    print(c)
    return render(request, 'cookies/home.html')

def delt(request):
    response = render(request, 'cookies/home.html')
    response.delete_cookie('user')
    return response
