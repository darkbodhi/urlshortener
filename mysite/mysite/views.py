from django.shortcuts import render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django import forms
from .models import *


class URLform(forms.Form):
    URL_link = forms.CharField(max_length=300)


def index(request):
    context = {
        "django_form": URLform
    }
    return render(request, "url_form/template/index", context)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        context = {
            "django_form": URLform
        }
        return render(request, "url_form/template/index", context)
    else:
        raise ValidationError("Error. Unknown request.")


def url_add(request, new_link):
    if request.method == "POST":
        url_link = URLform(request.POST)
        if URLValidator(url_link):
            mapping_urls(url_link)
            context = {
                "short link": "%s".format(new_link)}
            return render(request, "url_form/template/index", context)
        else:
            raise ValidationError("Error. Unknown request.")
    else:
        raise ValidationError("Error. Unknown request.")


def redirect_url(request, new_link):
    response = redirect('url_link')
    URL.hits_counter += 1
    return response

