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

from .models import Snippet
from .forms import SnippetForm


def home(request):
    return HttpResponse('Guardian BI Portal')

def presentation_page(request):
    return HttpResponse('Test presentation page')

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# def snippet_list(request):
#     photos = Snippet.objects.all()
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('photo_list')
#     else:
#         form = PhotoForm()
#     return render(request, 'album/photo_list.html', {'form': form, 'photos': photos})

