from django import forms
from .models import Work, Packages_work


class Packages_WorkForm(forms.ModelForm):
    class Meta:
        model = Packages_work
        fields = ('create',)
        widgets = {'create': forms.HiddenInput()}


class WorkForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'کار جدید را وارد کنید',
                                                          'dir':'rtl'}),label='')

    class Meta:
        model = Work
        fields = ('title','end_work')
        widgets = {'title': forms.HiddenInput(),'end_work':forms.HiddenInput()}
