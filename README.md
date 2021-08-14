## UserModule
### Main features
    - custom User model
    - forms for the custom user model
    - customized admin pannel

#### Link to know more about user model in offical django documentation
    - https://docs.djangoproject.com/en/3.2/ref/contrib/auth/

### DoctorERP
    - doctor model for doctors
    - doctor form - inherited from userform
    - patient model for patients with foreignkey to doctor model
    - patient form
        - inherited from userform
        - added doctor queryset field
        - Note: Must add 'doctor' to fields in meta-fields to make changes/save to model
    - templates
        - rendering form fields
        - passing urls parameters by {% url 'name' params=1 %}
    - dynamic url patterns
    - Getting all objects assign to a perticular object with foreignkey
        - i.e doctor - patient
        - to get all patient from doctor objects

### LogInOut
    - default forms like AuthenticationForm, PasswordChangeForm
        - more forms can be accessed if needed
    - updating users password logs out all sessions to update session again we need
        - i.e update_session_auth_hash(request, form.user)
    - changing a password with and without old password

### Group
    - custom user model with permissionsmixin
        - allows to create groups and permissions
    - admin pannel with groups model
    - add specific permission to the group
    - assigning group to user when it registers first time
    - check permisson in python and templates
        - python: if request.user.has_perm('user.delete_user')
        - template: perms.user.delete_user

### CookSess
    - cookies
        - get, set, delete method of normal cookies
        - with expire and age params
        - signed cookies with salt
    - Session
        - session uses database to store session
        - so need to add migrations
        - it stores session id as cookies in client side
        - default expiration is of 15 days
        - session can be stored in db/file/cache etc...
   
##### Link to know more about session
    - https://docs.djangoproject.com/en/3.2/topics/http/sessions/


### Signals
    - all built_in_signals are created in signal.py file
    - need to add ready method in apps.py and default_app_congfig in __init__.py
    - check extra args of that signal using the kwargs


### Profile
    - profile created on post_save signal
    - so it will not ceate profile for superuser
    - don't forget to pass *args, **kwargs to save method of profile model
    - need to add following in settings.py
        - MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # is location where we uploaded a file system
        - MEDIA_URL = '/media/' # public url of Media_root directory
    - need to add following in urls.py for loading image in tempalates
        - if settings.DEBUG: 
            - urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    - need to add following in template to rener image
        - <img src="{{ user.profile.img.url }}">
        - here img is name given to image field in profile model
    - userform and profile form can be different to update user and profile
    - by default django cares of changing the iamge name if it is already in assigned path. so every user will have different image and it's own

### PageCount
    - increases count on each request of that page

### Cache
    - to cahce entire site we need to add two line in middlewere
    - select storage system like database, file or memory etc
    - per-view cache is generated on url-basis means if two url will have a same view function then two differenct cache will be generated...

### Some important commands
    - to get IP of user
        - request.META.get('REMOTE_ADDR)
            - we can get it on user_logged_in signal
            - after getting we can stor it on session

    
            
    


    

