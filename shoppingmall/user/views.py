from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic import FormView
from .forms import RegisterForm,LoginForm
from .models import User

# Create your views here.
def index(request):
    return render(request, "user/index.html", {'id': request.session.get('user', ' ')})


def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    # auth.logout(request)
    return redirect('/')


class RegisterView(FormView):
    template_name = "user/register.html"
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        email = form.data.get('email')
        password = form.data.get('password')
        id = form.data.get('id')
        username = form.data.get('username')
        user = User(
            email=email,
            password=make_password(password),
            id = id,
            username = username

        )

        user.save()

        self.request.session['user'] = id
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('id')
        return super().form_valid(form)


