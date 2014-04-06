from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader


def root(request):
    my_variable = 69
    return render(request, 'index.html', locals())


def kr(request, pk):
	print pk, "fgfgfgj"
	return HttpResponse("ABC" + str(pk))


def company(request, pk):
	print pk, "pooplon"
	response = "andrew prestons likes to %s head" % pk
	#return HttpResponse(response)
	return render(request, 'company.html', locals())
