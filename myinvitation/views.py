# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import CridentialsForm
from django.shortcuts import render


def home(request):
    if request.POST:
        form = CridentialsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "myinvitation/home.html", {"message": "success"})
        else:
            return render(request, "myinvitation/home.html", {"message": "message success " + str(form.errors)})

    return render(request, 'myinvitation/home.html', {})
# {"status": "failed",
# "errors": form.errors})
