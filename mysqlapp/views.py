from django.shortcuts import render
from mysqlapp.forms import DocumentForm
from mysqlapp.models import Teacher
from django.views.generic import ListView

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

class Listview(ListView):
    model = Teacher
    template_name = "list.html"