# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Contract

# Create your views here.


def index(request):
    contracts = Contract.objects.all()
    context = {'contracts': contracts}
    return render(request, 'contracts/index.html', context)


def detail(request, contract_id):
    contract = Contract.objects.get(pk=contract_id)
    context = {'contract': contract}
    return render(request, 'contracts/contract_detail.html', context)
