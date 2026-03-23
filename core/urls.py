from django.urls import path
from . import views

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    path('library/', views.library, name='library'),

    # Authentication
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # Admin dashboard
    path('adminpage/', views.adminpage, name='adminpage'),
    path('upload_note/', views.upload_note, name='upload_note'),

    # Admin CRUD
    path('edit/<int:id>/', views.edit_note, name='edit_note'),
    path('delete/<int:id>/', views.delete_note, name='delete_note'),
]