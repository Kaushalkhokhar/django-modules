from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache


"""
Part 1: Per View Cache
1. This is per-view caching

2. Don't forget to uncomment two line in middlewere 
for caching the entire site


3. alternatively we can add per-view cache in urls.py file
like this..

    from django.views.decorators.cache import cache_page

    urlpatterns = [
        path('home/<int:code>/', cache_page(60 * 15)(views.home), name='home'),
    ]
"""
# @cache_page(time=, cache=, key_prefix=)
@cache_page(30)
def home(request):
    return render(request, 'view/home.html')

"""
Part 2: Low-level Cache API
"""
def test(request):
    song = cache.get('ttile')
    if song is None:
        cache.set('title', 'mai jaha rahu....', 20)
        # first args is key
        # second args is value
        # third is expires in seconds
        song = cache.get('title')
    # alternative of above code
    # song = cache.get_or_set('title', 'mai jaha rahu....', 20)
    return render(request, 'view/test.html', {'song': song})

"""
More:

cache.set('title', 'mai jaha rahu....', 20, version=some_integer)
here same key with different version can have different value
like:

cache.set('title', 'mai jaha rahu....', 20, version=1)
cache.set('title', 'ae vatan vatan....', 20, version=2)

this both are different. to get it we need to pass version also
like:
cache.get('title', version=1) will give 'mai jaha rahu....'
cache.get('title', version=2) will give 'ae vatan vatan....'
-------------------------
To delete cache:
cache.delete('title', version=1) will delete 'mai jaha rahu....'
-------------------------
To clear entire cache:
cache.clear()
"""