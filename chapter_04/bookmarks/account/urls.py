from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import user_login, dashboard, register

urlpatterns = [
    # path("login/", user_login, name="login")
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #
    # path("password-change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    # path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    #
    # path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path("passwrd-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path("password-reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('', include("django.contrib.auth.urls")),
    path('', dashboard, name="dashboard"),
    path("register/", register, name="register")
]
