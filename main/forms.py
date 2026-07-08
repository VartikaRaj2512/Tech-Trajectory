from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import LevelSelection

# Custom registration form
class RegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, label='Full Name')
    phone_number = forms.CharField(
        max_length=15,
        label='Phone Number',
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
    )
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone_number','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match")

        return cleaned_data


class LevelSelectionForm(forms.ModelForm):
    class Meta:
        model = LevelSelection
        fields = [
            'database_fundamentals', 'computer_architecture', 'distributed_computing_systems',
            'cyber_security', 'networking', 'software_development', 'programming_skills', 
            'data_analyst', 'computer_forensics_fundamentals', 'technical_communication',
            'ai_ml', 'software_engineering', 'business_analysis', 'communication_skills',
            'data_science', 'troubleshooting_skills', 'graphics_designing'
        ]