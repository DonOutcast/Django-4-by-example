from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd.get("username"),
                password=cd.get("password")
            )
            if user is not None:
                login(request, user)
                return HttpResponse("Authenticated successfully")
            else:
                return HttpResponse("Disabled account")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


@login_required
def dashboard(request):
    return render(
        request,
        "account/dashboard.html",
        {"section": "dashboard"}
    )


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data.get("password")
            )
            new_user.save()
            return render(
                request,
                "account/register_done.html",
                {"new_user": new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        "account/register.html",
        {"user_form": user_form}
    )
