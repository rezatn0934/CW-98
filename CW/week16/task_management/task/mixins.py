from .models import Task


class TodoOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['pk'])
        if not request.user.is_authenticated or not task.user == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
