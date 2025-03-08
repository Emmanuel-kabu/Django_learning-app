from django.shortcuts import render,redirect,get_object_or_404
from .models import Course
from .forms import CourseForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, resolve
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
# Create your views here.
def index(request):
    """Learning platform homepage"""
    return render(request, 'MylearningApp/index.html')

def privacy(request):
    """our privacy policy"""
    return render(request, 'MylearningApp/privacy.html')

def support(request):
    """ contact us for support"""
    return render(request, 'MylearningApp/support.html')

def t_and_c(request):
    """ Our terms and condition"""
    return render(request, 'MylearningApp/t_and_c.html')

def faq(request):
    """ frequently asked questions"""
    return render(request, 'MylearningApp/faq.html')

def about(request):
    """About us"""
    return render(request, 'MylearningApp/about.html')

def profile(request):
    """profile of the user"""
    return render(request, 'MylearningApp/profile.html')

def notifications(request):
    """notifications"""
    return render(request, 'MylearningApp/notification.html')

def testimonials(request):
    """what our users say about us """
    return render(request, 'MylearningApp/testimonial.html')

def community(request):
    """ your community"""
    return render(request, 'MylearningApp/community.html')

def notification(request):
    """ your notifications """
    return render(request, 'MylearningApp/notification.html')
    
def home(request):
    """ your meeting"""
    return render(request, 'MylearningApp/home.html')




# views for the course
def course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        form.is_valid()
    
        
        format = form.cleaned_data.get('format')
        slides = form.cleaned_data.get('slides')
        content = form.cleaned_data.get('content')

        if format == 'slide' and not slides:
            form.add_error('slides', 'This field is required for slide-based course')
        elif format == 'text' and not content:
            form.add_error('content', 'This field is required for a text-based text') 
        else:
           return HttpResponseRedirect(reverse('MylearningApp:course'))
    else:
        form = CourseForm()
        
    context = {'form' : form}
    return render(request, 'MylearningApp/course.html', context) 



def custom_upload_file(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES('upload')
        file_name = default_storage.save(upload.name, upload)
        url = default_storage.url(file_name)
        return JsonResponse({'url':url})
    return JsonResponse({'error': 'invalid request'}, status = 400)


      
       

 








               




    


