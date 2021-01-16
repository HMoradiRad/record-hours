from django import forms
from .models import Work, Packages_work


class Packages_WorkForm(forms.ModelForm):
    class Meta:
        model = Packages_work
        fields = ('create',)
        widgets = {'create': forms.HiddenInput()}


class WorkForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کار جدید را وارد کنید',
                                      'dir': 'rtl'}), label='')

    class Meta:
        model = Work
        fields = ('title',)
        widgets = {'title': forms.HiddenInput()}


class WorkForms(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('end_work',)
        widgets = {'end_work': forms.HiddenInput()}
