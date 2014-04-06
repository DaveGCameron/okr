from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader


def root(request):
    return HttpResponse("yuss boobs")

def company(request, pk):
	print pk, "pooplons"
	response = "andrew prestons likes to %s head" % pk
	return HttpResponse(response)
