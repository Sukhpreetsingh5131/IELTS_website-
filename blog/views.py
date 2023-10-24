from django.shortcuts import render
from.models import email
from.models import Review
from django.http import HttpResponseRedirect
import re

def first_page(request):
    books=email.objects.all()


    return render(request,'index.html',{'names':books})
def detail_info(request,id):
    book=email.objects.get(pk=id)
    return render(request,'detail.html',{
        'names':book.name,
        'no':book.no

    })
def blogs_open(request):
    return render(request,'advance.html')
def about(request):

    return render(request,'about.html')
def post_home(request):
   
   

    return render(request,'home.html')
def post_student(request):

    return render(request,'student_detail.html')

def reviews(request):
    
    has_error = False
    if request.method == 'POST':
        entered_mail = request.POST.get('email')
        entered_password = request.POST.get('password')
        
        
        # Print the entered values
        print("Entered email:", entered_mail)
        print("Entered password:", entered_password)
        
        # Save the data in the database
        new_review = Review(user_mail=entered_mail, password=entered_password)
        new_review.save()

        return render(request,'thankyou.html')

    return render(request, 'forms.html')
def guru(request):
    return render(render,'thankyou.html')


def thankyou(request):
    return render(request, 'userform/thankyou.html')


def teacher(request):
    return render(request,'teacher.html')



# Create your views here.
