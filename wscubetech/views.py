from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForm
from service.models import Service
from news.models import News
from enquiry.models import Enquiry
from django.core.paginator import Paginator

def HomePage(request):
    return render(request, 'index.html')

def FoodsPage(request):
    return render(request, 'foods.html')

def OrderPage(request):
    return render(request, 'order.html')

def CategoriesPage(request):
    return render(request, 'categories.html')

def UserFormPage(request):
    var_userform = UserForm()
    data = {
        'userform_key' : var_userform
    }
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            
            print("Username : " + username + " Name : " + name + " Email : " + email)
            
            return HttpResponseRedirect('/')
    except:
        pass
        
    
    return render(request, 'userform.html', data)

def SubmitUserFormPage(request):
    return HttpResponse(request)
    

def aboutus(request):
    return HttpResponse("Welcome to Django!")

def courses(request):
    all_courses = Service.objects.all()
    news_data = News.objects.all()
    
    paginator = Paginator(all_courses, 2)
    page_number = request.GET.get('page')
    all_courses_data = paginator.get_page(page_number)
    
    if request.method == 'GET':
        search_title = request.GET.get('servicename')
        if search_title:
            all_courses_data = Service.objects.filter(service_title__icontains=search_title)
    
    data = {
        'courses': all_courses_data,
        'news': news_data,
    }
    return render(request, 'courses.html', data)

def NewsDetailsPage(request, slug):
    news_details_data = News.objects.get(slug=slug)
    data = {
        'selected_news': news_details_data,
    }
    return render(request, 'newsdetails.html', data)

def courseDetails(request, courseid):
    return HttpResponse(f"{courseid}-th Course.")



def enquiry_form(request):
    if request.method == 'POST':
        form = Enquiry(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry_success')
    else:
        form = Enquiry()
    
    return render(request, 'templates/enquiry_form.html', {'form': form})

def enquiry_success(request):
    return render(request, 'templates/enquiry_success.html')