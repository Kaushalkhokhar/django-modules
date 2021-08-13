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

    

