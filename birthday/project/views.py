from django.shortcuts import render, redirect, get_object_or_404
from.forms import CommentForm, CreateUserForm
from .models import Comment, Author, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms import inlineformset_factory
from .decorators import unauthenticated_user

def get_author(user):
    qs =Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def semarang(request):
    return render(request, 'semarang.html')

def contact(request):
    return render(request, 'contact.html')

def schedule(request):
    return render(request, 'schedule.html')

def surat(request):
    surat = Comment.objects.all()
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.surat = surat
            form.save()
            return redirect('surat')
    context = {
        'surat': surat,
        'form': form
    }
    return render(request, 'surat.html', context)

def dufan(request):
    return render(request, 'dufan.html')

def tickets(request):
    return render(request, 'tickets.html')

def kotatua(request):
    return render(request, 'kotatua.html')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register_fix.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



