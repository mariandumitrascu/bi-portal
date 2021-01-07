from django import forms
from django.core.files import File

from PIL import Image

from .models import Snippet



class SnippetForm(forms.ModelForm):
    x = forms.IntegerField(
        widget=forms.HiddenInput()
        )
    y = forms.IntegerField(
        widget=forms.HiddenInput()
        )
    w = forms.IntegerField(
        widget=forms.HiddenInput()
        )
    h = forms.IntegerField(
        widget=forms.HiddenInput()
        )

    class Meta:
        model = Snippet
        fields = ('image_cropped', 'x', 'y', 'w', 'h', )


        widgets = {
            'file': forms.FileInput(attrs={
                'accept': 'image/*'  # this is not an actual validation! don't rely on that!
            })
        }

    def save(self):
        this_snippet = super(SnippetForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('w')
        h = self.cleaned_data.get('h')

        image_tmp = Image.open(this_snippet.image_cropped)

        cropped_image = image_tmp.crop((x, y, w+x, h+y))

        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(this_snippet.cropped_image.path)

        return this_snippet

