from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
from .forms import UserLoginForm
"""the app_name variable provided for {% url 'namespace-for-url-ofproject:the nameofviewinpath' and relate it with id%}"""
app_name='accounts'


urlpatterns = [

    path("register/", views.account_register, name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="accounts/registeration/login.html", form_class=UserLoginForm),name="login",),
    path("logout/", auth_views.LogoutView.as_view(next_page="/accounts/login/"), name="logout"),
    path("profile/edit/", views.edit_details, name="edit_details"),
    path("profile/show/", views.show_details, name="show_details"),
]
