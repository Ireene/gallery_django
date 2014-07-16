from django import forms
from models import Album, Image, Comment

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ('title', 'public')

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('title', 'summary','image', 'albums', 'user')
        
class CommentForm(forms.ModelForm):
        
    class Meta:
        model = Comment
        fields = ('name', 'body')