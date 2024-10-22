from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from project.models import Theme, Message
from project.forms import UserRegisterForm, ThemeForm, MessageForm

from django.contrib.auth import get_user_model

User = get_user_model()


@login_required(login_url="login")
def home_view(request: WSGIRequest):
    if request.method == "POST":
        form = ThemeForm(request.POST, request.FILES)

        if form.is_valid():
            new_theme: Theme = form.save(commit=False)
            new_theme.owner = request.user

            new_theme.save()

        else:
            print(form.errors)

    themes = Theme.objects.all()
    form = ThemeForm()
    context = {"themes": themes, "theme_form": form}

    return render(request, "home.html", context)


@login_required(login_url="login")
def theme_view(request: WSGIRequest, pk: int):
    theme = get_object_or_404(Theme, pk=pk)
    user = request.user

    if request.method == "POST":
        form = MessageForm(request.POST)

        if "message-id" in request.POST:
            # eski habar yangilanyapti

            message = get_object_or_404(Message, pk=request.POST["message-id"])
            form = MessageForm(request.POST, instance=message)

        if form.is_valid():
            message: Message = form.save(commit=False)

            message.theme = theme
            message.sender = user

            message.save()

        else:
            print(form.errors)

    form = MessageForm()
    theme_form = ThemeForm()
    context = {"theme": theme, "form": form, "theme_form": theme_form}

    return render(request, "theme.html", context)


@login_required(login_url="login")
def user_profile(request: WSGIRequest):

    user = request.user

    if request.method == "POST":

        for key, value in request.POST.items():
            print(key, value, hasattr(user, key), hasattr(user.profile, key))

            if hasattr(user, key):
                setattr(user, key, value)

            if hasattr(user.profile, key):
                setattr(user.profile, key, value)

        user.profile.save()
        user.save()

    user = request.user

    context = {"user": user}

    return render(request, "profile.html", context)


@login_required(login_url="login")
def profile(request: WSGIRequest, pk: int):

    user = get_object_or_404(User, pk=pk)

    context = {"user": user}

    return render(request, "profile.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")
