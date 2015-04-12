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
from Connect_FMS.forms import *
from django.contrib.auth.models import User, UserProfile
from django import forms


def index(request):
    context = {}
    context['post'] = Post.objects.all()
    return render(request,'Connect_FMS/index.html', context)

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        context = {}
        errors = []
        context['errors'] = errors
        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            # profile = profile_form.save(commit=False)
            UserProfile.objects.save(user=user.id)
            # profile.user = user

            # profile.save()
            context['user'] = user
            return render(request, 'Connect_FMS/index.html', context)
        else:
            return render(request, 'login.html', context)

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

    from myblog.forms import PostForm
 
def post_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
          new_post = form.save()
        return HttpResponseRedirect(reverse('index'))

 
    return render(request, 'Connect_FMS/post_form_upload.html', {
        'form': form,
    })