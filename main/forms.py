from django import forms
from main.models import UserRegister

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['f_name'].label = 'First Name'
        self.fields['l_name'].label = 'Last Name'
        self.fields['email_id'].label = 'Email Address'
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
    class Meta:
        model = UserRegister
        fields = ['f_name', 'l_name', 'email_id', 'username', 'password']
        
