from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from okr.models import Company


def root(request):
    companies = Company.objects.all()
    return render(request, 'index.html', locals())


def kr(request, pk):
    my_variable = 9
    return render(request, 'KR', locals())


def company(request, pk):
    company = Company.objects.get(pk=pk)
    my_employees = company.employee_set.all()
    return render(request, 'company.html', locals())
