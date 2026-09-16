from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings_view, name='settings'),

    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path(
        'students/<int:pk>/edit/',
        views.student_update,
        name='student_update'),
    path(
        'students/<int:pk>/delete/',
        views.student_delete,
        name='student_delete'),

    # Achievement URLs
    path('achievements/add/', views.achievement_add, name='achievement_add'),
    path(
        'achievements/add/<int:student_pk>/',
        views.achievement_add,
        name='achievement_add_for_student'),
    path(
        'achievements/<int:pk>/edit/',
        views.achievement_update,
        name='achievement_update'),
    path(
        'achievements/<int:pk>/delete/',
        views.achievement_delete,
        name='achievement_delete'),
    path(
        'achievements/<int:pk>/status/<str:status>/',
        views.update_achievement_status,
        name='achievement_status_update'),

    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
]
