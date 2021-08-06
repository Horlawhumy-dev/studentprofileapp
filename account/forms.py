from django import forms
from .models import StudentAccount

class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentAccount
        fields = ['name', 'email', 'phone']