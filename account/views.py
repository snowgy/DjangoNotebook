
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from . import models
from account.models import User

# Create your views here.


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User()
            user.username = username
            user.password = password
            user.save()
            return render(request, 'success.html',)
    else:
        uf = UserForm()

    return render(request, 'sign_up.html', {'uf': uf})


def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username=username, password=password)
            user2 = User.objects.get(username=username, password=password)
            if user:
                user_id = user2.id
                return render(request, 'home.html', {'user_id': user_id})
            else:
                return render(request, 'fail.html')
    else:
        uf = UserForm
    return render(request, 'login.html', {'uf': uf})