from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# Connecting a view to a template
def simple_view(request):
    return render(request, 'the_network/example.html')
