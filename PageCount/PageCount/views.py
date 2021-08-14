from django.shortcuts import HttpResponse

def home(request):
    c = request.session.get('count', 0)
    new_c = c + 1
    request.session['count'] = new_c
    return HttpResponse(f'Count: {new_c}')