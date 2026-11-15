from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        widgets = {'text': forms.Textarea(attrs={'rows': 7, 'class': 'form-control'})}
        help_texts = {'group': 'Группа, к которой будет относиться запись.'}
