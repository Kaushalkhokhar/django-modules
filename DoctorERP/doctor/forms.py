from .models import Doctor
from user.forms import UserAdminCreationForm

class RegisterDoctorForm(UserAdminCreationForm):
    # password1 = models.CharField(label='Password', widgets=forms.PasswordInput)
    # password2 = models.CharField(label='Confirm Password', widgets=forms.PasswordInput)

    class Meta(UserAdminCreationForm.Meta):
        model = Doctor
        fields = ['email', 'first_name', 'last_name']
