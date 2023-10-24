from django.shortcuts import render
from django.http import HttpResponseRedirect
from profiles.models import personal_detail

def speaking(request):
    personal=personal_detail.objects.all()


    return render(request,'writing_check.html',{'info':personal})
# Create your views here.
def store_feedback(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        writing_content = request.POST.get('writing-content')
        feedback = request.POST.get('feedback')
        errors = request.POST.get('errors')
        score = request.POST.get('score')
        recording = request.FILES.get('recording')

        feedback_instance = Feedback(
            name=name,
            email=email,
            age=age,
            gender=gender,
            writing_content=writing_content,
            feedback=feedback,
            errors=errors,
            score=score,
            recording=recording
        )
        feedback_instance.save()

        return render(request,'param.html') # Redirect to a success page

   

def essay_detail(request, essay_id):
    print('sukh')
    eassay_full = personal_detail.objects.get(id=essay_id)
    print(eassay_full.comments)
    return render(request, 'eassay.detail.html', {'eassay_full': eassay_full})

   





