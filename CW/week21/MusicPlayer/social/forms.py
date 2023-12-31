from django import forms
from .models import Comment, Playlist


class CommentCreation(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class PlaylistCreation(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('title',)
        labels = {'title': ''}
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'creatPlaylist'})
        }
