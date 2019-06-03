from django import forms
from mysqlapp.models import Teacher

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"