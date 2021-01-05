from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView, ListView, UpdateView, View
from django.views.generic import TemplateView

# Create your views here.


def home(request):
    return HttpResponse('Guardian BI Portal')

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
