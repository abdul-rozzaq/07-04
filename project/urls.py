from django.urls import path

from .views import home_view, theme_view, register, user_login, user_logout, user_profile, profile


urlpatterns = [
    path("", home_view, name="home"),
    path("theme/<int:pk>/", theme_view, name="theme_view"),
    
    path("profile/", user_profile, name="profile"),
    path("profile/<int:pk>/", profile, name="profile"),
    
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]
