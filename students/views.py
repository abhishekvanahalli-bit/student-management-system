from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (AchievementForm, CategoryForm, ProfileUpdateForm,
                    StudentForm, UserUpdateForm)
from .models import Achievement, Category, Student


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(
                request, 'Registration successful! Welcome to the dashboard.')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'students/profile.html')


@login_required
def settings_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            profile = p_form.save()

            # Update session for immediate effect
            request.session['theme_mode'] = profile.theme_mode
            request.session['brightness'] = profile.brightness
            request.session['accent_color'] = profile.accent_color

            messages.success(request, 'Settings updated successfully!')
            return redirect('settings')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Settings'
    }
    return render(request, 'students/settings.html', context)


@login_required
def dashboard(request):
    total_students = Student.objects.count()
    total_achievements = Achievement.objects.count()
    total_categories = Category.objects.count()
    recent_achievements = Achievement.objects.order_by('-created_at')[:5]

    context = {
        'total_students': total_students,
        'total_achievements': total_achievements,
        'total_categories': total_categories,
        'recent_achievements': recent_achievements,
    }
    return render(request, 'students/dashboard.html', context)

# Student Views


@login_required
def student_list(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request,
                  'students/student_list.html',
                  {'students': students})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    achievements = student.achievements.all()
    return render(request, 'students/student_detail.html',
                  {'student': student, 'achievements': achievements})


@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html',
                  {'form': form, 'title': 'Add Student'})


@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html',
                  {'form': form, 'title': 'Update Student'})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html',
                  {'object': student, 'title': 'Delete Student'})

# Achievement Views


@login_required
def achievement_add(request, student_pk=None):
    student = None
    if student_pk:
        student = get_object_or_404(Student, pk=student_pk)

    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)
        if form.is_valid():
            achievement = form.save()
            messages.success(request, 'Achievement added successfully!')
            return redirect('student_detail', pk=achievement.student.pk)
    else:
        initial = {}
        if student:
            initial['student'] = student
        form = AchievementForm(initial=initial)

    return render(request, 'students/achievement_form.html',
                  {'form': form, 'title': 'Add Achievement'})


@login_required
def achievement_update(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        form = AchievementForm(
            request.POST,
            request.FILES,
            instance=achievement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Achievement updated successfully!')
            return redirect('student_detail', pk=achievement.student.pk)
    else:
        form = AchievementForm(instance=achievement)
    return render(request, 'students/achievement_form.html',
                  {'form': form, 'title': 'Update Achievement'})


@login_required
def achievement_delete(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    student_pk = achievement.student.pk
    if request.method == 'POST':
        achievement.delete()
        messages.success(request, 'Achievement deleted successfully!')
        return redirect('student_detail', pk=student_pk)
    return render(request, 'students/confirm_delete.html',
                  {'object': achievement, 'title': 'Delete Achievement'})


@login_required
def update_achievement_status(request, pk, status):
    achievement = get_object_or_404(Achievement, pk=pk)
    if status in ['Approved', 'Rejected', 'Pending']:
        achievement.status = status
        achievement.save()
        messages.success(request, f'Achievement status updated to {status}!')
    return redirect('student_detail', pk=achievement.student.pk)

# Category Views


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request,
                  'students/category_list.html',
                  {'categories': categories})


@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'students/category_form.html',
                  {'form': form, 'title': 'Add Category'})
