from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, Tutor

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, 
                            help_text="Required. Enter a valid email address.")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_image', 'learning_language', 'proficiency_level', 'chosen_field', 'assigned_tutor')
        widgets = {
            'learning_language': forms.Select(attrs={'class': 'form-select'}),
            'proficiency_level': forms.Select(attrs={'class': 'form-select'}),
            'chosen_field': forms.Select(attrs={'class': 'form-select'}),
            'assigned_tutor': forms.Select(attrs={'class': 'form-select'}),
        }

class UserUpdateForm(forms.ModelForm):
    """Form for updating user information like username and email"""
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if username and User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

class CustomPasswordChangeForm(PasswordChangeForm):
    """Custom password change form with Bootstrap styling"""
    
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'}) 