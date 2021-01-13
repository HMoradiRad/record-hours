from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from .models import Work, Packages_work
from .forms import WorkForm, Packages_WorkForm
from django.conf import settings
from django.contrib.auth.decorators import login_required


def all_works(request):

    works = Work.objects.all()
    packages = Packages_work.objects.all()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts:user_login')
        iform = WorkForm(request.POST)
        if iform.is_valid():
            iform.save()
            return redirect('http://127.0.0.1:8000/')
    if request.method == 'POST':
        bform = Packages_WorkForm(request.POST)
        if bform.is_valid():
            bform.save()
            return redirect('http://127.0.0.1:8000/')

    else:
        iform = WorkForm()
        bform = Packages_WorkForm()

    return render(request, 'hours/all_works.html',
                  {'works': works, 'iform': iform, 'packages': packages, 'bform': bform})
