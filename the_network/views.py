from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}


def news(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404('GENERIC ERROR')


def page_num_view(request, num_pg):
    topics_list = list(articles.keys())  # ['sports', 'finance', 'politics']#
    topic = topics_list[num_pg]

    webpage = reverse('topic-page', args=[topic])
    return HttpResponseRedirect(webpage)


