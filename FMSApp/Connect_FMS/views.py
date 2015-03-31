from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader

def index(request):
    return render(request, 'index.html')

def view(request):
    return render(request, 'view.html')

def vote(request, post_id):
    p = get_object_or_404(Post, id=post_id)
    p.upvote
    return render(request, 'views.html')