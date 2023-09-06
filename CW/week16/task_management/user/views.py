from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password
from django.views import View
from .forms import UserForm, ChangePassForm
from .mixins import ProfileMixin


class UserLogin(LoginView):
    redirect_authenticated_user = True
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('home_page')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user, backend='user.authentication.AuthBackend')
        return super().form_invalid(form)


def register_user(request):
    message = None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user, backend='user.authentication.AuthBackend')
            return redirect('/')
    elif request.method == "GET":
        form = UserForm()
    return render(request, "user/login.html", {"message": message, "form": form})


class ProfileView(ProfileMixin, View):
    temp_name = 'user/profile.html'


class ChangePassView(View):
    temp_name = 'user/changePass.html'
    form_model = ChangePassForm

    def get(self, request):
        form = self.form_model()
        return render(request, self.temp_name, {'form': form})

    def post(self, request):
        form = self.form_model(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            old_pass = cd['old_password']
            pass1 = cd['password1']
            pass2 = cd['password2']
            if old_pass == request.user.password:
                if pass1 and pass2 and pass1 == pass2:
                    user = request.user
                    user.password = pass1
                    user.save()
                messages.error(request, "Your new password didn't match!")
            else:
                messages.error(request, "Your old password didn't match!")
        return redirect('profile')