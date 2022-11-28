from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from App1.models import Avatar

class Armazones_Formulario(forms.Form):
    marca = forms.CharField()
    color = forms.CharField()
    material = forms.CharField()
    tamaño = forms.CharField()
    precio = forms.IntegerField()
    código = forms.IntegerField()
    medidas = forms.CharField()
    tipo = forms.CharField()
    peso = forms.CharField()
    estilo = forms.CharField()
    fecha = forms. DateField()
    foto = forms.ImageField(required = False)


class Sol_Formulario(forms.Form):
    marca = forms.CharField()
    color_armazón = forms.CharField()
    color_lente = forms.CharField()
    material = forms.CharField()
    tamaño = forms.CharField()
    precio = forms.IntegerField()
    código = forms.IntegerField()
    medidas = forms.CharField()
    tipo = forms.CharField()
    peso = forms.CharField()
    polarizado = forms.CharField()
    antireflejo = forms.CharField()
    estilo = forms.CharField()
    fecha = forms. DateField()
    foto = forms.ImageField(required = False)


class Lentes_Formulario(forms.Form):
    marca = forms.CharField()
    color = forms.CharField()
    material = forms.CharField()
    graduación = forms.IntegerField()
    precio = forms.IntegerField()
    código = forms.IntegerField()
    laboratorio = forms.CharField()
    duración = forms.CharField()
    prescripción = forms.CharField()
    fecha = forms. DateField()
    foto = forms.ImageField(required = False)


class User_Edit_Form(UserChangeForm):
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2


class User_Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class User_Profile_Form(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]