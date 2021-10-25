from django.shortcuts import render
from rest_framework import generics


def home(request):
    return render(request, "index.html", {})
