from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


    def clean_password2(self):

        print('self\n',self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')
        
class ContactForm(forms.Form):
    
    nombre = forms.CharField(label='Nombre', required=True)
    
    email = forms.CharField(label='Email', required=True)
    
    servicio = forms.CharField(label='Servicio')
    
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)