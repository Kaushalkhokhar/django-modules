from django.http.response import HttpResponse

# Create your views here.
def home(request):
    print("This is home view")
    return HttpResponse("Hello we are testing middlewete...")

def about(request):
    print("This is about view")
    return HttpResponse("Hello we are testing middlewete...")