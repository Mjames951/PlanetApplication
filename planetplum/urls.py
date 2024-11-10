from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user/<username>/', views.userProfile, name='userProfile'),
    path('editUserProfile/', views.editUserProfile.as_view(), name='editUserProfile'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name='about'),
    path('bands/', views.bands.as_view(), name='bands'),
]