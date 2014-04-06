from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader


def root(request):
    my_variable = 69
    return render(request, 'index.html', locals())


def kr(request, pk):
	my_variable = 9
	return render(request, 'KR', locals())


def company(request, pk):
	print pk, "pooplons"
	response = "andrew prestons likes to %s head" % pk
	return HttpResponse(response)

