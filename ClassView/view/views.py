from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.views import View


class Home(View):
    """
    url will be like = path('home/, views.home.as_view())
    """
    def get(self, request):
        # form = ExampleForm()
        return HttpResponse('Hello World...')

class MyHome(Home):
    """
    This is inherited from home view
    """
    def post(self, request):
        # form = ExampleForm(request.POST)
        # if form.is_valid():
            # ...
        return HttpResponse('Hello World...')

class HomeTemplateView(TemplateView):
    template_name = 'apps/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)