from django.db.models import Exists, OuterRef

from social.models import Like


class LikeMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.annotate(
                liked=Exists(Like.objects.filter(song=OuterRef('pk'), user=self.request.user))
            )
        return queryset