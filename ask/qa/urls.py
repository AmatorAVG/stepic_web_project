from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.test, name='index'),
    path('question/<int:id>/', views.test, name='question'),
    # path('login/', views.test, name='login'),
    re_path(r'^login\/.*$', views.test),
    path('signup/', views.test, name='signup'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='new'),
]