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
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import permission_required

# home feed page, passes in all posts, votes, and responses
@login_required
def index(request):
    context = {}
    context['posts'] = Post.objects.all()
    context['userVotes'] = Votes.objects.filter(user=request.user)
    context['statuses'] = Status.objects.all()
    context['responses'] = Response.objects.all()
    return render(request,'Connect_FMS/index.html', context)

# validate and create new user
@csrf_protect
def register(request):
    # render Registration form
    if request.user.is_authenticated():
        return HttpResponseRedirect( 'feed/')
    elif request.method == 'GET':
        reg_form = RegistrationForm()
        return render(request, 'Connect_FMS/signup.html', {'form1':reg_form})
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
            user.save()

            # set role to student default in UserProfile subclass
            UserProfile.objects.create(user=user, role='student')

            # automatically log them in
            user = auth.authenticate(username=user.username, password=request.POST.get('password', ''))
            user.addStudentPermissions()
            if user is not None:
                auth.login(request, user)
                return render(request, 'Connect_FMS/index.html', {'form': AuthenticationForm()})
            else:
                HttpResponse('authentication failed')
                # return render(request, 'Connect_FMS/login.html', {'form': AuthenticationForm()})
        else:
            print 'Form is not valid'
            return render(request, 'Connect_FMS/signup.html', {'form1': RegistrationForm()})
    return render(request, 'Connect_FMS/signup.html', {'form1': reg_form})

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect( 'feed/')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
        reg_form = RegistrationForm()
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            # request.user.message_set.create(message="You're logged in")
            return HttpResponseRedirect('feed/')
        else:
            return HttpResponseRedirect('login.html')
    return render(request, 'Connect_FMS/login.html', {'form':login_form})

def logout(request):
    auth.logout(request)
    login_form = AuthenticationForm()
    reg_form = RegistrationForm()
    context = {}
    context['form'] = login_form
    context['form1'] = reg_form
    return render(request, 'Connect_FMS/login.html', context)

def about(request):
    context = {}
    return render(request, 'Connect_FMS/about.html', context)

@login_required
def details(request, post_id):
    try:
        p = Post.objects.get(pk=post_id)
        context = {}
        context['singlepost'] = p
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'Connect_FMS/details.html', context)

@permission_required('Connect_FMS.permission.can_add_vote')
@login_required
def post_vote(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id', '')
        post_id = request.POST.get('post_id', '')
        p = Post.objects.get(pk=post_id)
        u = User.objects.get(pk=user_id)
        flag = request.POST.get('flag', '')
        try: 
            v = Votes.objects.filter(post=p, user=u)[0]
            v.vote = flag
            v.save()
        except:
            v = Votes.objects.create(post=p, user=u, vote=flag)
            v.save()
        return HttpResponseRedirect(reverse('feed'))
    return render(request, 'Connect_FMS/index.html')

@permission_required('Connect_FMS.permission.can_add_post_comment')
@login_required
def submit_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('description')
        post_id = request.POST.get('post')
        p=Post.objects.get(pk=post_id)
        PostComment.objects.create(user=request.user, post=p, description=comment)
        return HttpResponseRedirect(reverse('feed'))
    return render(request, 'Connect_FMS/index.html')

@login_required
def post_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    elif request.method == 'POST':
        # A POST request: Handle Form Upload
        form = PostForm(request.POST, request.FILES) 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            Votes.objects.create(user=new_post.user, post=new_post)
            return HttpResponseRedirect(reverse('feed'))
    return render(request, 'Connect_FMS/post_form_upload.html', {'form': form})

@login_required
def status_upload(request):
    if request.method == 'GET':
        form = StatusForm()
    elif request.method == 'POST':
        form = StatusForm(request.POST, request.FILES)
        if form.is_valid():
            new_status = form.save(commit=False)
            new_status.user = request.user
            new_status.save()
            return HttpResponseRedirect(reverse('feed'))
    return render(request, 'Connect_FMS/status_upload.html', {'form': form})

def create_status(request):
    return render(request, 'Connect_FMS/index.html')