from django.db import models
from django.contrib.auth.models import User
from extentions.utils import jalali_converter, t_jlali_converter
from django.utils import timezone


class Packages_work(models.Model):

    create = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def j_created_at(self):
        return jalali_converter(self.create)


class Work(models.Model):
    title = models.CharField(max_length=200)
    start_work = models.DateTimeField(default=timezone.now)
    end_work = models.DateTimeField(blank=True,null=True)
    work_duration = models.PositiveIntegerField(default=0)
    package_work = models.ForeignKey(Packages_work, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    def j_start_work(self):
        return t_jlali_converter(self.start_work)

    def j_end_work(self):
        return t_jlali_converter(self.end_work)
