from django import forms
from .models import NotesModel


class NewNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = ''
        self.fields['body'].widget.attrs['placeholder'] = ''
        self.fields['summary'].widget.attrs['placeholder'] = ''
       
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = NotesModel
        fields = ('title', 'body','summary','is_private')

