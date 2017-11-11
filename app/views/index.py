# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..forms import UploadFileForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'index.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        # if form.is_valid():
        return HttpResponseRedirect(reverse('app:index'))
    else:
        form = UploadFileForm()
    return HttpResponseRedirect(reverse('app:index'))
