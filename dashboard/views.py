from django.shortcuts import render
from .forms import phase_1Form
from django.http import HttpResponseRedirect

# Create your views here.

def dashboard(request):
	return render(request,'dashboard.html')

def phase_1_upload(request):
    if request.method == 'POST':
        form = phase_1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('index')
    else:
        form = phase_1Form()
    return render(request, 'Phase_1_Form.html', {
        'form': form
    })
	
	


