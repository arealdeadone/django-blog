from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateFrom, CounsellorDetailsUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Profile


def register(request):

    if request.user.is_authenticated:
        return redirect('blog-home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)
        c_form = CounsellorDetailsUpdateForm(request.POST, instance=request.user.counsellordetails)

        if u_form.is_valid() and p_form.is_valid() and c_form.is_valid():
            u_form.save()
            p_form.save()
            c_form.save()
            if p_form.cleaned_data.get('is_counsellor'):
                messages.success(request, 'Your account has been updated! Now You can add counsellor details')
                return redirect('profile')
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)
        c_form = CounsellorDetailsUpdateForm(instance=request.user.counsellordetails)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'c_form': c_form
    }
    return render(request, 'users/profile.html', context)


class Counsellors(ListView):
    model = User
    paginate_by = 8
    context_object_name = 'counsellors'

    def get_queryset(self):
        return Profile.objects.filter(is_counsellor=True)
