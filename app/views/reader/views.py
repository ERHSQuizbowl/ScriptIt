# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from scriptit.settings import MEDIA_ROOT
from app.scripts.parse_script import ParseScript


def main(request):
    filename = request.GET.get("file")
    file = MEDIA_ROOT + '/' + filename
    parser = ParseScript(file)
    parser.parse(file)

    return render(request, 'reader.html', context={'sound': MEDIA_ROOT + '/sound.mp3'})
