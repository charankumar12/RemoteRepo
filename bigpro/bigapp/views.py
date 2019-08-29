from django.shortcuts import render
from .models import ServicesData,FeedbackData,EnquiryData
from .forms import FeedbackForm
from .forms import EnquiryForm
import datetime as dt
date1=dt.datetime.now()

from django.http.response import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def enquiry(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            courses=eform.cleaned_data.get('courses')

            data=EnquiryData(
                Name=name,
                Mobile=mobile,
                Email=email,
                gender=gender,
                courses=courses,
                #shifts=shifts
            )
            data.save()
            eform=EnquiryForm()
            return render(request,'contact.html',{'eform':eform})
        else:
                      return HttpResponse("User Invalid dATA")

    else:
        eform=EnquiryForm()
        return render(request,'contact.html',{'eform':eform})

def feedback(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')

            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date= date1
            )
            data.save()
            fform = FeedbackForm()
            feedbacks=FeedbackData.objects.all()

            return render(request,'feedback.html',{'fform':fform ,'feedbacks':feedbacks})
        else:
            return HttpResponse('User Invalid Data')
    else:
        fform = FeedbackForm()
        feedbacks=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})

def gallery(request):
    return render(request,'gallery.html')

def services(request):
    services=ServicesData.objects.all()
    return render(request,'services.html',{'services':services})