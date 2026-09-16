from django import forms
from django.contrib.auth.models import User

from .models import Achievement, Category, Profile, Student


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
            'bio',
            'theme_mode',
            'background_image',
            'accent_color',
            'brightness']
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'}),
            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3}),
            'theme_mode': forms.Select(
                attrs={
                    'class': 'form-select'}),
            'background_image': forms.FileInput(
                attrs={
                    'class': 'form-control'}),
            'accent_color': forms.TextInput(
                attrs={
                    'type': 'color',
                    'class': 'form-control form-control-color'}),
            'brightness': forms.NumberInput(
                attrs={
                    'type': 'range',
                    'min': '50',
                    'max': '100',
                    'class': 'form-range'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'register_number',
            'course',
            'batch',
            'department',
            'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'register_number': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'batch': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3}),
        }


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = [
            'student',
            'title',
            'description',
            'proof',
            'category',
            'date',
            'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'proof': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
