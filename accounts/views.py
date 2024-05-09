from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Profile
from django.urls import reverse
from .forms import RegistrationForm, UserEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required




@login_required
def edit_details(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST,request.FILES,instance=request.user)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, "accounts/dashboard/edit_details.html", {"user_form": user_form})


@login_required
def show_details(request):
    profile = Profile.objects.get(email=request.user.email)
    return render(request,'accounts/dashboard/show_details.html',{'profilevar': profile})




def account_register(request):

    if request.user.is_authenticated:
         return redirect("accounts:show_details")

    if request.method == "POST":
        registerForm = RegistrationForm(request.POST,request.FILES)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data["email"]
            user.name = registerForm.cleaned_data["name"]
            user.date_of_birth = registerForm.cleaned_data["date_of_birth"]
            user.set_password(registerForm.cleaned_data["password"])
            user.save()
            return redirect('/accounts/login')
    else:
        registerForm = RegistrationForm()
    return render(request, "accounts/registeration/register.html", {"form": registerForm})
