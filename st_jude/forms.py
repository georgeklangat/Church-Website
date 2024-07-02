# from django import forms
# from django.forms import ModelForm
# from .models import Registration
#
#
# class RegisterForm(ModelForm):
#     class Meta:
#         model = Registration
#         fields = ('first_name', 'last_name', 'surname', 'password1', 'password2')
#         labels = {
#             'first_name': '',
#             'last_name': '',
#             'surname': '',
#             'password1': '',
#             'password2': '',
#
#         }
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Second Name'}),
#             'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
#             'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter  the password'}),
#             'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reenter the password'})
#
#         }
