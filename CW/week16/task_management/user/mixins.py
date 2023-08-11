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
        form = self.form_model(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')


class ImageMixin:
    def change_image(self, old_instance, field):
        target = getattr(old_instance, field)

        if (not target == getattr(self, field) and
                target and os.path.exists(target.path)):
            os.remove(target.path)

    def delete_image(self, field):
        target = getattr(self, field)
        if os.path.exists(target.path):
            os.remove(target.path)
