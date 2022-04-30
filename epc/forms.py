from django import forms
from django.forms import TextInput
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empid', 'name', 'dept', ]
        labels = {'empid': 'EmployeeId', 'name': 'Enter name', 'dept': 'Department'}
