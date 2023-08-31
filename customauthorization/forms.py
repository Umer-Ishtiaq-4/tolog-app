from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomUserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add 'form-control' class to username and password input fields
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        # Updating Labels
        # self.fields['username'].label = "Custom Username Label"
        # self.fields['password'].label = "Custom Password Label"
        # self.fields['password'].help_text = "Custom Password Help Text"
    
    class Meta:
        model = User
        fields = ['username', 'password']  # Include other fields as needed



class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add 'form-control' class to username and password input fields
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

        
    username = forms.CharField(
        label="Username",
        help_text="",
        error_messages={
            'unique': "This username is already taken. Please choose a different one.",
        }
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,  # Prevent password from being automatically stripped of leading/trailing spaces
        help_text="Enter a strong password with at least 8 characters.",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    # Override password2 field
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,  # Prevent password from being automatically stripped of leading/trailing spaces
        help_text="Re-enter the password.",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Include other fields as needed
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password1': forms.Select(attrs={'class': 'form-control'}),
        #     'password2': forms.Select(attrs={'class': 'form-control'}),
        # }
