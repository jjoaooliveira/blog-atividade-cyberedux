from django.forms import ModelForm
from .models import post, comentario
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = comentario
        fields = ['nome', 'email', 'conteudo']

class PostForm(ModelForm):
    class Meta:
        model = post
        fields = ['titulo','conteudo', 'resumo', 'img']

for fd in PostForm.base_fields:
    PostForm.base_fields[fd].widget.attrs["class"] = "form-control" 