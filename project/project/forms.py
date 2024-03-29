from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    f_name = forms.CharField(required=True)
    # extra info about class
    class Meta:
        model = User
        fields = ('username', 'email', 'f_name', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.f_name = self.cleaned_data['f_name']
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save()
            
        return user        