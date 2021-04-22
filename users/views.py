from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render

from .forms import UserRegisterForm, EditUserForm, EditProfileForm


def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('chapters:index'))


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form
        form = UserRegisterForm()
    else:
        # Process completed form.
        form = UserRegisterForm(data=request.POST)
        p_form = EditProfileForm(data=request.POST)
        if form.is_valid():

            new_user = form.save()
            # Log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            new_profile = p_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return HttpResponseRedirect(reverse('chapters:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        post_data = request.POST or None
        file_data = request.FILES or None
        form = EditUserForm(post_data, instance=request.user)
        p_form = EditProfileForm(post_data, file_data, instance=request.user.profile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = EditUserForm(instance=request.user)
        p_form = EditProfileForm(instance=request.user.profile)
    context = {'form': form, 'p_form': p_form}
    print(p_form)
    return render(request, 'users/profile.html', context)
