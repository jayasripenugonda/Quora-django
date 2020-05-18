from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name='homepage'),
    path('homepage.html/', views.homepage, name='homepage'),
    path('register.html/', views.register, name='register'),
    path('login.html/', views.login, name='login'),
    path('profile.html/', views.profile, name='profile'),
    path('update_profile.html/', views.updateprofile, name='updateprofile'),
    path('Answer.html/', views.answerquestion, name='answerquestion'),
    path('ask_question.html/', views.askquestion, name='askquestion'),
    path('about.html/', views.about, name='about'),

]
