from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('add-category', views.Register.as_view(), name="register_view"),
    path('list-categories', views.LoginView.as_view(), name="login_view"),
    path('update-category', views.RefreshToken.as_view(), name="refresh_token_view"),
    path('delete-category', views.Logout.as_view(), name="logout_view"),
]

# Register, login, refresh token, logout, change password, recover password
