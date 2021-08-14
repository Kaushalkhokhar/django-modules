from django.shortcuts import HttpResponse


"""
We need to add middleware to settins.py file
"""

from django.http.response import HttpResponse


def my_middleware(get_response):

    """
    Code written here will be execited only once when first time app starts
    """
    print('This is initializarion')

    def my_function(request):
        """
        Code written here will be executed before the view-function
        """
        print("Before view")

        response = get_response(request)
        """
        Code written here will be executed after the view-function
        """
        print("After view")

        return response

    return my_function

"""
Class based middleware
"""
class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    """
    Code written here will be execited only once when first time app starts
    """
    print('This is initializarion of class based')

    def __call__(self, request):
        """
        Code written here will be executed before the view-function
        """
        print("Before view")

        response = self.get_response(request)
        """
        Code written here will be executed after the view-function
        """
        print("After view")

        return response

class MyMiddlewareTwo:

    def __init__(self, get_response):
        self.get_response = get_response

    """
    Code written here will be execited only once when first time app starts
    """
    print('This is initializarion of class based two...')

    def __call__(self, request):
        """
        Code written here will be executed before the view-function
        """
        print("Before view two...")

        # response = self.get_response(request)
        response = HttpResponse("Response from second middleware...") # to give response from here..
        # it will not allow ro propagate request to next middleware/view 
        """
        Code written here will be executed after the view-function
        """
        print("After view two...")

        return response

class MyMiddlewareThree:

    def __init__(self, get_response):
        self.get_response = get_response

    """
    Code written here will be execited only once when first time app starts
    """
    print('This is initializarion of class based three...')

    def __call__(self, request):
        """
        Code written here will be executed before the view-function
        """
        print("Before view three...")

        response = self.get_response(request)
        """
        Code written here will be executed after the view-function
        """
        print("After view three...")

        return response