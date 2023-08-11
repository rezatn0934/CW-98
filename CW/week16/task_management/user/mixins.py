from .models import CustomUser
from django.shortcuts import render, redirect
from .forms import UpdateUser


class ProfileMixin:
    temp_name = None
    form_model = UpdateUser

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_model(instance=request.user)
        return render(request, self.temp_name, {"form": form})

    def post(self, request):
        form = self.form_model(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)
            img = request.POST.get('image')
            user.image = img
            user.save()
            return redirect('profile')
