from django import forms
from .models import Ator, Conexao

class AtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = ['nome', 'link_imagem', 'descricao']



# class ConexaoForm(forms.ModelForm):
#     class Meta:
#         model = Conexao
#         fields = ['conexaoA', 'conexaoB']

# from django import forms
# from .models import Conexao, Ator

class ConexaoForm(forms.ModelForm):
    conexaoA = forms.ModelChoiceField(queryset=Ator.objects.all(), label="Conexão A")
    conexaoB = forms.ModelChoiceField(queryset=Ator.objects.all(), label="Conexão B")

    class Meta:
        model = Conexao
        fields = ['conexaoA', 'conexaoB']