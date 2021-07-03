from django.urls import path, re_path

from . import views
app_name = 'qa'
urlpatterns = [
    path('', views.NewView, name='index'),
    path('question/<int:id>/', views.QuestionView, name='question'),
    path('login/', views.LoginView, name='login'),
    re_path(r'^login\/.*$', views.test),
    path('signup/', views.SignupView, name='signup'),
    path('ask/', views.question_add, name='ask'),
    path('popular/', views.PopularView, name='popular'),
    path('new/', views.test, name='new'),
]