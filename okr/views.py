from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader


def root(request):
    return HttpResponse("yuss boobs")

def kr(request, pk):
	print pk, "fgfgfgj"
	return HttpResponse("ABC" + str(pk))


