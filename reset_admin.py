import os
import django

# Set up Django environment BEFORE importing models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from django.contrib.auth.models import User
from students.models import Profile # Also import Profile to ensure it exists

def create_admin():
    username = 'Abhishek' # Target the 'Abhishek' user
    email = 'abhishek@example.com' # You can change this if needed
    password = '***ROTATED***'
    
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f"Password for existing user '{username}' has been reset to '{password}'")
    else:
        # If 'Abhishek' user doesn't exist, create it as a superuser
        user = User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created successfully with password '{password}'")

    # Ensure the profile exists for this user
    profile, created = Profile.objects.get_or_create(user=user)
    if created:
        print(f"Profile created for user: {user.username}")
    else:
        print(f"Profile already exists for user: {user.username}")

if __name__ == '__main__':
    create_admin()
