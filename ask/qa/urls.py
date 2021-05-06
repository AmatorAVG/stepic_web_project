from django.urls import path, re_path

from . import views
app_name = 'qa'
urlpatterns = [
    path('', views.NewView, name='index'),
    path('question/<int:id>/', views.QuestionView, name='question'),
    # path('login/', views.test, name='login'),
    re_path(r'^login\/.*$', views.test),
    path('signup/', views.test, name='signup'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.PopularView, name='popular'),
    path('new/', views.test, name='new'),
]