from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = messages.success(request, f"Your account has been created {username}!")
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    context = {
        'forms': form
    }
    return render(request, 'users/register.html', context)


def profile(request):
    return render(request, "users/profile.html")


