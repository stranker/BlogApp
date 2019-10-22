from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.TextInput()

    class Meta:
        model = Comment
        fields = ['content']
