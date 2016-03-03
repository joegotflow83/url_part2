from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from accounts import views

urlpatterns = [
    url(r'^login/', auth_views.login, name='login'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'^logout/', login_required(auth_views.logout), {'next_page': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'},  name='logout'),
]
