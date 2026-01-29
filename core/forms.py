from django import forms
from .models import LoginForm, Booking

class Login(forms.ModelForm):
    class Meta:
        model = LoginForm
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'