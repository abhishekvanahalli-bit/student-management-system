from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    THEME_CHOICES = (
        ('light', 'Light'),
        ('dark', 'Dark'),
        ('auto', 'Auto'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(blank=True)

    # Premium Settings
    theme_mode = models.CharField(
        max_length=10,
        choices=THEME_CHOICES,
        default='auto')
    background_image = models.ImageField(
        upload_to='backgrounds/',
        blank=True,
        null=True,
        help_text="Upload a custom background for your dashboard.")
    accent_color = models.CharField(
        max_length=7,
        default='#4e73df',
        help_text="Hex code for UI accent color.")
    brightness = models.IntegerField(
        default=100, help_text="UI Brightness percentage (50-100).")

    def __str__(self):
        return f'{self.user.username} Profile'


class Student(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    register_number = models.CharField(max_length=50, unique=True)
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.register_number})"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Achievement(models.Model):
    STATUS_CHOICES = (
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='achievements')
    title = models.CharField(max_length=255)
    description = models.TextField()
    proof = models.FileField(upload_to='proofs/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='achievements')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending')

    def __str__(self):
        return f"{self.title} - {self.student.name}"
