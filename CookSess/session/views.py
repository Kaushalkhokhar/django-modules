from datetime import datetime, timedelta
from django.shortcuts import render, resolve_url

def set(request):
    request.session['user'] = 'kush'
    request.session['account'] = 'demo'
    # request.session.set_expiry(10) 
    # expiry can be different value. To know more read 
    # documetaion in link given in README.md
    return render(request, 'session/home.html')

def get(request):
    user = request.session.get('user')
    account = request.session.get('account')
    print(user, account)
    print(help(request.session))
    return render(request, 'session/home.html')

def delt(request):
    # del request.session['user'] # to delete specific value
    # to completely delete session we can use flush
    request.session.flush() # deletes active session
    request.session.clear_expired() # deletes expired session
    return render(request, 'session/home.html')