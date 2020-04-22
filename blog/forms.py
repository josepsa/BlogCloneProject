from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text')

    widgets ={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),  ##This textinputclass is for CSS
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}) ##editable,medium-editor-textarea are bootstrap
        # class and postcontent is our own css class
    }


class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')

    widgets = {
        'author': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
    }
