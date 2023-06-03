from django.forms import ModelForm

from forms.models import Form


class FormModelForm(ModelForm):

    class Meta:
        model = Form
        fields = ('name', 'question')
