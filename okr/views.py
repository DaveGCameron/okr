from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader


def root(request):
    return HttpResponse("yuss boobs")


