from django import forms

from .models import Worker, Tool


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('name', 'name_fam', 'years_old',)


class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ('name', 'worker', 'inv_number', 'cost',)
