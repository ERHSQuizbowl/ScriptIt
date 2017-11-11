# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..forms import DocumentForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'index.html')


def upload_file(request):
    if request.method == 'POST':
        myfile = request.FILES['myFile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # return render(request, 'index.html')
        tocat = "%s?file=" + myfile.name
        return HttpResponseRedirect(tocat % reverse('app:reader'))
    else:
        form = DocumentForm()
    return render(request, 'index.html', context={'form': form})
    # return HttpResponseRedirect(reverse('app:index'))
