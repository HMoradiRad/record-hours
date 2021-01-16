from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from .models import Work, Packages_work
from .forms import WorkForm, Packages_WorkForm, WorkForms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import Http404


def add_new_task(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts:user_login')
        iform = WorkForm(request.POST)
        if iform.is_valid():
            pk = request.POST.get("package_id")
            package = Packages_work.objects.get(pk=pk)
            last_work = Work.objects.filter(package_work=package).last()

            form = iform.save(commit=False)
            form.package_work = package
            form.save()

            if last_work:
                last_work.end_work = timezone.now()
                last_work.save()
            return redirect('http://127.0.0.1:8000/work/{}/'.format(pk))
    else:
        raise Http404("not found")


def end_task(request):
    if request.method == 'POST':
        pk = request.POST.get("id")
        package = request.POST.get("package_id")
        work = Work.objects.get(pk=pk)
        work.end_work = timezone.now()
        work.save()
        return redirect('http://127.0.0.1:8000/work/{}/'.format(package))
    else:
        raise Http404("not found")


def task_new_package(request):
    if request.method == 'POST':
        pform = Packages_WorkForm(request.POST)
        if pform.is_valid():
            pform.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        raise Http404("not found")


def main(request):
    packages = Packages_work.objects.all()

    iform = WorkForm()
    bform = Packages_WorkForm()
    eform = WorkForms()

    return render(request, 'hours/all_packages.html',
                  {'iform': iform, 'packages': packages, 'bform': bform, 'eform': eform})


def work(request, pk):
    package_id = pk
    works = Work.objects.filter(package_work=package_id)
    packages = Packages_work.objects.all()

    iform = WorkForm()
    bform = Packages_WorkForm()
    eform = WorkForms()

    return render(request, 'hours/work.html',
                  {'works': works, 'iform': iform, 'packages': packages, 'bform': bform, 'eform': eform,
                   'package_id':package_id})
