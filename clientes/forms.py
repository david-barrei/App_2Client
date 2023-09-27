from socket import fromshare
from django import forms
from .models import Cliente


class ClientesForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields= '__all__'

    def __init__(self, *args,**kwargs):
        super(ClientesForm,self).__init__(*args, **kwargs)
        self.fields['lenguaje'].empty_label="Selecciona"
        self.fields['SO'].empty_label="Selecciona"
        self.fields['area'].empty_label="Seleciona"
        self.fields['ap'].required=True
        self.fields['am'].required=False






