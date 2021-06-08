from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth import views as auth_views
from . views import LoginsView

urlpatterns = [
    path('register/', views.register, name='register' ),
    path('login/', LoginsView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/', views.profile, name="profile")
]