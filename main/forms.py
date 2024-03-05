from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

##################################### Validation Functions #####################################
def password_validation(value):
    if len(value) < 8 :
        raise ValidationError('Password must contain 8 characters')
    if not any(char.isupper() for char in value):
        raise ValidationError('Password must contain at least one upper case')
    if not any(char.islower() for char in value):
        raise ValidationError('Password must contain at least one lower case')
    if not any(char in '@/_' for char in value):
        raise ValidationError('Password must contain any one special character from \'@/_\'')
    
############################################# Forms ############################################
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        password_validation(password)
        return password

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    