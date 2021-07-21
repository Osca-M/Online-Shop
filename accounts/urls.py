from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path('create-account', views.Register.as_view(), name="register_view"),
    path('login', views.LoginView.as_view(), name="login_view"),
    path('refresh-token', views.RefreshToken.as_view(), name="refresh_token_view"),
    path('logout', views.Logout.as_view(), name="logout_view"),
    path('profile', views.ProfileView.as_view(), name="profile_view"),
    path('change-password', views.ChangePasswordView.as_view(), name="change_password_view"),
]

# Register, login, refresh token, logout, change password, recover password
