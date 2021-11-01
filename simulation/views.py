from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics


def home(request):
    return render(request, "index.html")
