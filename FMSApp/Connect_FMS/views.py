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
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    context = {}
    context['post'] = Post.objects.all()
    return render(request,'Connect_FMS/index.html', context)

# create new user and log them in
def register(request):
    # render Registration form
    if request.method == 'GET':
        reg_form = RegistrationForm()
    # when trying to login create and save user and redirect to feed
    elif request.method == 'POST':
        reg_form = RegistrationForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        context = {}
        errors = []
        context['errors'] = errors
        if reg_form.is_valid():
            user = reg_form.save()

            # hash password with django default method
            user.set_password(user.password)
            user.save()

            # set role to student default in UserProfile subclass
            UserProfile.objects.save(user=user.id)

            context['user'] = user
            return render(request, 'Connect_FMS/index.html', context)
        else:
            return render(request, 'Connect_FMS/login.html', {'form': reg_form})
    return render(request, 'Connect_FMS/login.html', {'form':reg_form})

def login(request):
    if request.method == 'GET':
        login_form = AuthenticationForm()
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('Connect_FMS/index.html')
        # else:
            # return HttpResponseRedirect('/accounts/invalid')
    return render(request, 'Connect_FMS/login.html', {'form':login_form})

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
    elif request.method == 'POST':
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
          new_post = form.save()
        return HttpResponseRedirect(reverse('index'))
 
    return render(request, 'Connect_FMS/post_form_upload.html', {
        'form': form,
    })