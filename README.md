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
    



    

