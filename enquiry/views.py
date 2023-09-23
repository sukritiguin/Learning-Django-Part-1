from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from .models import Enquiry
from .models import Enquiry
from .forms import EnquiryForm

# Create your views here.
def enquiry_form(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry_success')
    else:
        form = EnquiryForm()
    
    return render(request, '../templates/enquiry_form.html', {'form': form})

def enquiry_success(request):
    return render(request, '../templates/enquiry_success.html')