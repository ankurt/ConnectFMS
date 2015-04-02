from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader
from Connect_FMS.models import *
from django.conf import settings


def index(request):
    context = {}
    context['post'] = Post.objects.all()
    return render(request,'Connect_FMS/index.html', context)

def details(request, post_id):
    try:
        p = Post.objects.get(pk=post_id)
        context = {}
        context['singlepost'] = p
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'Connect_FMS/details.html', context)

def vote(request, post_id):
    p = get_object_or_404(Post, id=post_id)
    p.upvote
    return render(request, 'views.html')