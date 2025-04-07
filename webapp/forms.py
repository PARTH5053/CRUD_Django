from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput,TextInput
from .models import Records

# ----- register/create User -----
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

# ----- Login User -----
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['first_name','last_name','email','phone','address','city','province','country']

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['first_name','last_name','email','phone','address','city','province','country']
