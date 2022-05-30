from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic, View

from .forms import LoginForm, UserRegisterForm


def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'User with this email already has been')
        if User.objects.filter(username=username).first():
            form.add_error('username', 'This username is already taken')
        elif form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            messages.success(request, 'Account successfully created!')
            return render(request, 'users/register.html')
        else:
            messages.error(request, 'error')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
