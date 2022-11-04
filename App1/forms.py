from django import forms


class Sol_Formulario(forms.Form):
    marca = forms.CharField()
    color_armazón = forms.CharField()
    color_lente = forms.CharField()
    material = forms.CharField()
    tamaño = forms.CharField()
    precio = forms.IntegerField()
    código = forms.IntegerField()


class Lentes_Formulario(forms.Form):
    marca = forms.CharField()
    color = forms.CharField()
    material = forms.CharField()
    graduación = forms.IntegerField()
    precio = forms.IntegerField()
    código = forms.IntegerField()