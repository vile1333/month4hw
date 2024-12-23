from django.http import HttpResponse
from django.shortcuts import render
from . import models,forms
from django.views import generic
from .models import LitresModel

class LitresListView(generic.ListView):
    template_name = 'litres/litres.html'
    context_object_name = 'litres'
    model = models.LitresModel

    def get_queryset(self):
        return LitresModel.objects.all().order_by('-id')

class LitresFormView(generic.FormView):
    template_name = 'litres/litres_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('STATUS 200')
        else:
            return super(LitresFormView, self).post(request, *args, **kwargs)

# Create your views here.
