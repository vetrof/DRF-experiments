from django.shortcuts import render
from django.views.generic import CreateView

from forms.forms import FormModelForm
from forms.models import Form


class QuestionPage(CreateView):
    template_name = 'question.html'
    form_class = FormModelForm
    success_url = '/'

