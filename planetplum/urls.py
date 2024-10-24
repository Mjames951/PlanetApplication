from django.urls import path
from . import views
from . import secretViews
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name='about'),
]