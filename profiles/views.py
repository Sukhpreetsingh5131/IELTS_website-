from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponseRedirect
from.models import personal_detail
from.models import User
from.models import create_room
from liveroom.models import personal_rooms
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse

#now 


    





def save_file(file):
    with open('temp/image.jpg','wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    

class createprofile(View):

    def get(self,request):
        return render(request,'profiles_test.html')
    def post(self,request):
        profile=userprofile(image=request.FILES['images'])
        print(profile)
        profile.save()
        return HttpResponseRedirect('/profiles')

def profile_list(request):
    
    profiles = userprofile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'viewprofile.html', context)

def thankyou(request):
    return render(request,'thankyou.html')
def writing(request):
    return render(request,'writing.html')
# views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect


def submit_basic_info(request):
    print('harmeet')


    return render(request, 'success.html') 
def param(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        comment = request.POST.get('comment')

        new= personal_rooms(name=name,email=email, age=age, gender=gender, comments=comment)
        new.save()

        print(name)
        print(email)
        print(age)
        print(gender)
        print(comment)
        return render(request,'param.html')
  # Process the comment data as needed
    else:
        # Handle other request methods or render a response for GET requests
        print('no')
def speaking(request):
    return render(request,'speaking.html') 
import random
from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client
from django.shortcuts import render, HttpResponse
from twilio.rest import Client
import random

from django.shortcuts import render, HttpResponse
from twilio.rest import Client
import random

def send_otp(request):
    if request.method == 'POST':
        # Get the submitted form data
        country_code = request.POST.get('country_code')
        phone_number = request.POST.get('phone_number')
        request.session['phone_number'] = phone_number
        request.session['country_code'] = country_code
        return render(request,'success.html')

        # Check if the phone number is valid
        if(len(phone_number))!=10 and country_code=='+91':
            error_message = 'Please enter a valid phone number.'
            return render(request, 'speaking.html', {'error_message': error_message})
 
        if(len(phone_number)==10 and country_code!='+91'):
            error_message='please enter valid country code .'
            return render(request,'speaking.html',{'error_message':error_message})
        

        # Generate a random OTP
        otp = str(random.randint(1000, 9999))

        # Customize the message from your company
        company_message = 'Welcome to visit this application. Your OTP is:'

        # Send the OTP via SMS using Twilio
        account_sid = 'AC7e8303a70fe4ff4a6e20ffbe9ba6098a'
        auth_token = 'e84a9176abd4e8cb0985504f88beb0e5'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f'{company_message} {otp}',
            from_='+15416278150',
            to=f'{country_code}{phone_number}'
        )

        # Check if the SMS was sent successfully
        if message.sid:
            # Render the OTP verification page with the OTP details
            request.session['phone_number'] = phone_number
            request.session['country_code'] = country_code
            request.session['otp'] = otp
            return render(request, 'param.html', {'phone_number': phone_number})
        else:
            # Handle the case when SMS sending fails
            return HttpResponse('Failed to send OTP via SMS')

    # Render the initial form page
    return render(request, 'speaking.html')


import random
from django.shortcuts import render, HttpResponse
from twilio.rest import Client

def resend_otp(request):
    # Generate a new OTP
    otp = str(random.randint(1000, 9999))
    phone_number = request.session.get('phone_number')
    country_code=request.session.get('country_code')
    print(phone_number)

    if phone_number:
        print('sukh')
        # Customize the message from your company
        company_message = 'Welcome to visit this application. Your new OTP is:'

        # Send the new OTP via SMS using Twilio
        account_sid = 'AC7e8303a70fe4ff4a6e20ffbe9ba6098a'
        auth_token = 'e84a9176abd4e8cb0985504f88beb0e5'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f'{company_message} {otp}',
            from_='+15416278150',
            to=f'{country_code}{phone_number}'
        )

        # Check if the SMS was sent successfully
        if message.sid:
            request.session['otp'] = otp
            text='otp has been sent  !'
            return render(request, 'param.html',{'texts':text})
        else:
            # Handle the case when SMS sending fails
            return HttpResponse('Failed to send new OTP via SMS')
    else:
        print('kawal')
        # Handle the case when phone_number is not in the session
        return HttpResponse('Phone number not found in session.')

def otp_check(request):
    if request.method == 'POST':
        print('1')
        # Get the submitted form data
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        # Combine the OTP digits
        entered_otp = otp1 + otp2 + otp3 + otp4
        print(entered_otp)

        # Retrieve the phone number and generated OTP from the session
        phone_number = request.session.get('phone_number')
        generated_otp = request.session.get('otp')

        # Check if the entered OTP matches the generated OTP
        if generated_otp and entered_otp == generated_otp:
            # OTP is correct, perform further actions or redirect
            print('right')
            return render(request, 'success.html', {'phone_number': phone_number})
        else:

            # OTP is incorrect, display an error message or redirect
            return render(request, 'error.html')

    # Render the OTP verification form page
    return render(request, 'otp_check.html')


from django.shortcuts import render, redirect
from .models import User

# views.py
def register_user(request):
    if request.method == 'POST':
        phone_number = request.session.get('phone_number')
        country_code = request.session.get('country_code')
        user_name = request.POST.get('username')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile=(request.FILES.get('profile_picture'))
        
        print(profile)
        request.session['email']=email


        # Create a User instance with the form data
        user = User(
            phone_number=phone_number,
            country_code=country_code,
            user_name=user_name,
            gender=gender,
            gmail=email,
            password=password
        )

        # Check if a profile picture is provided and assign it to the User instance
        
        # Save the User instance to the database
        user.save()

        # Clear the session data
        #del request.session['phone_number']
        del request.session['country_code']

        return render(request, 'home_app.html')  # Replace 'home_app' with the desired URL name for the home page
    else:
        error_message = ''

    return render(request, 'registration_form.html', {'error_message': error_message})
from django.shortcuts import render
import random
from django.shortcuts import render, redirect
import random
import uuid
import time


from django.shortcuts import render, redirect, get_object_or_404

def room_opens(request, room_id):
    print('ggod sir')
    

    if request.method == 'POST':

        print('mount')
        print(room_id)
         # Retrieve the title and tag values from the query parameters
        title = request.POST.get('title')
        selected_tag = request.POST.get('selected_tag')
        print(title)
        print(selected_tag)
        appId='2728d387e56746329bcbf35121610d2a'
        appCertificate='47ddc21b21b94a31a52c52a0870a7f5a'
        channelName=str(room_id)
        expirationTimeInSeconds=3600*24
        currentTimeStamps=time.time()
        privilegeExpiredTs=currentTimeStamps+expirationTimeInSeconds
        role=1
        email = request.session.get('email')
        uid=email
        token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
        print(token)

        phone_number = request.session.get('phone_number')
        email = request.session.get('email')
        print(email)
        
        user_profile = User.objects.get(gmail=email)
        followers = 0
        user_name_live = user_profile.user_name
        
        create_rooms = create_room(user_name=user_name_live, tag=selected_tag, text=title, followers=followers,room_ide=room_id,token=token)
        create_rooms.save()
        host=True
        return render(request,'chat.html')
       
    else:
 
          email = request.session.get('email')
          print(email)
          title_room=create_room.objects.get(room_ide=room_id)
          title=title_room.text
          selected_tag=title_room.tag
          token=title_room.token
          user_profile = User.objects.get(gmail=email)
          user_name_live = user_profile.user_name
          host=False
          return render(request,'chat.html',{'channelName': room_id, 'token': token, 'userName': user_name_live})
def reading(request):
    return render(request,'reading.html')
def create_dynamic_room(request):
    if request.method == 'POST':
        # Retrieve the title and tag values from the form
        title = request.POST.get('title')
        selected_tag = request.POST.get('selected_tag')

        # Generate a random room ID (channel name) using 6 characters
        room_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

        # Agora App Credentials
        APP_ID = 'd9b053b43560494e8c634884cf413e06'
        APP_CERTIFICATE = '47ddc21b21b94a31a52c52a0870a7f5a'
        # Generate token
        expiration_time_in_seconds = 3600 * 24
        current_timestamp = int(time.time())
        privilege_expired_ts = current_timestamp + expiration_time_in_seconds
        role = RtcTokenBuilder.Role.PUBLISHER  # Assuming users can publish audio
        uid = room_id  # Use the room ID as the UID for simplicity
        token = RtcTokenBuilder.build_token_with_uid(APP_ID, APP_CERTIFICATE, room_id, uid, role, privilege_expired_ts)

        # Get the user's name from the session or wherever it is stored
        user_name_live = "John Doe"  # Replace this with the actual user's name

        # Save room details to the database
        create_rooms = create_room(user_name=user_name_live, tag=selected_tag, text=title, room_ide=room_id)
        create_rooms.save()

        # Return the room ID (channel name), token, and user's name in the JSON response
        return JsonResponse({'channelName': room_id, 'token': token, 'userName': user_name_live})

    else:
        # Handle GET request if needed
        return JsonResponse({'message': 'Method not allowed'}, status=405)


import time
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
from .models import User, create_room

def chat(request):
    APP_ID = 'd9b053b43560494e8c634884cf413e06'
    appCertificate = '47ddc21b21b94a31a52c52a0870a7f5a'
    
    channel_name = request.GET.get('channel')
    user_name = request.GET.get('user_name')
    
    expiration_time_in_seconds = 3600 * 24
    current_time_stamps = int(time.time())
    privilege_expired_ts = current_time_stamps + expiration_time_in_seconds
    role = 1

    user_profile = User.objects.get(user_name=user_name)  # Replace with the appropriate way to get the user profile
    uid = user_profile.id  # Assuming the user ID is the UID
    
    token = RtcTokenBuilder.build_token_with_uid(
        APP_ID, appCertificate, channel_name, uid, role, privilege_expired_ts
    )
    
    response_data = {
        'token': token
    }
    
    return JsonResponse(response_data)

     
def chats(request):
    return render(request,'chat.html')  
def redirect_to_room(room_id):
    return redirect('room_open', room_id=room_id)

def community(request):
     
     rooms = create_room.objects.all()
     return render(request, 'room_list.html', {'rooms': rooms})
def writing_ai(request):
    return render(request,'writing_ai.html')
#here in this code we will validate an eassay with chat gpt ai 



def evaluate_writing(request):
    print('sukh...')


    if request.method == 'POST':

        # Retrieve user inputs from the POST data
        user_name = request.POST.get('userName')
        user_email = request.POST.get('userEmail')
        user_mobile = request.POST.get('userMobile')
        essay_heading = request.POST.get('essayHeading')
        essay_content = request.POST.get('essayContent')
        print(user_email)
        print(user_name)
        print(user_mobile)
        print(essay_heading)
        print(essay_content)
        feedback=chat_gpt_open_ai(essay_heading,essay_content)
        analyze_score(feedback)
        #we nee dto set the tiitle as well

        for key, value in feedback.items():

            if '**' in value:



                parts = value.split('**')
                if len(parts) > 2:


                    title, content = parts[1], parts[2]
                    feedback[key] = {'title': title, 'content': content}
                else:


                    feedback[key] = {'title': None, 'content': value}
            else:


                feedback[key] = {'title': None, 'content': value}

        colors = ["color1", "color2", "color3", "color4", "color5"]
        context={
            'feedback':feedback,
            'colors': colors

        }
        

        return render(request, 'writing_mistakes.html',context)


           


       



        
def analyze_score(dict_feedback):
    json_rules=[
  {
    "band": 9,
    "task_achievement": ["fully satisfies all requirements", "clearly presents a developed response"],
    "coherence_and_cohesion": ["uses cohesion seamlessly", "skillfully manages paragraphing"],
    "lexical_resource": ["uses wide vocabulary naturally", "rare minor errors as 'slips'"],
    "grammatical_range_and_accuracy": ["uses wide range of structures", "rare minor errors as 'slips'"]
  },
  {
    "band": 8,
    "task_achievement": ["covers all requirements", "presents key features clearly"],
    "coherence_and_cohesion": ["sequences information logically", "manages cohesion well"],
    "lexical_resource": ["uses wide vocabulary fluently", "uses uncommon lexical items skillfully"],
    "grammatical_range_and_accuracy": ["uses wide range of structures", "mostly error-free sentences"]
  },
  {
    "band": 7,
    "task_achievement": ["covers requirements", "clear purpose with consistent tone"],
    "coherence_and_cohesion": ["logically organises information", "some under/over-use of devices"],
    "lexical_resource": ["uses varied vocabulary", "some errors in word formation"],
    "grammatical_range_and_accuracy": ["uses complex structures", "frequent error-free sentences"]
  },
  {
    "band": 6,
    "task_achievement": ["addresses the task", "overview with information"],
    "coherence_and_cohesion": ["clear progression", "some faulty sentences"],
    "lexical_resource": ["adequate vocabulary range", "makes some spelling errors"],
    "grammatical_range_and_accuracy": ["mix of simple and complex forms", "some grammar errors"]
  }
]

    api_key = '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'
    openai.api_key = api_key
    prompts="""
    Given the feedback dictionary:
{dict_feedback}

And the IELTS writing band score descriptors:
{json_rules}

Analyze the feedback and descriptors to provide an evaluation for the user's essay:

Determine and assign a band score (from 1 to 9, including half scores like 6.5, 7.5, etc.) for each of the following criteria: 
- coherence and cohesion
- lexical resources
- task response
- grammatical range and accuracy.

Provide the results ONLY in the structured format:
{'grammar': [BAND_SCORE],'lexical': [BAND_SCORE],'task_response': [BAND_SCORE],'coherence_and_cohesion': [BAND_SCORE]}

Do not include any extra text or information.



    """
      
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompts,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        generated_list = response.choices[0].text
        print('--------')
        print('shery')
        print(generated_list)
        print('mata')
     

    
    except Exception as e:
        print("Error:", e)
        return None, None
  
        



#here in this function we will evaluate 


import openai
import re

def chat_gpt_open_ai(essay_heading, essay_content):
    api_key = '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'
    openai.api_key = api_key
    
    prompts = f"""
    Please evaluate the following IELTS essay and provide structured feedback:

**Essay Heading:** "{essay_heading}"

**Essay Content:**
"{essay_content}"

1. **Grammar Mistakes:**
   - Identify and list all grammatical errors present in the essay.
  

2. **Lexical Resources:**
   - Identify any opportunities to use more advanced vocabulary and expressions.
  

3. **Task Response:**
   - Evaluate the essay's response to the essay prompt and task requirements.
   - Provide feedback on how well the essay addresses the task and stays on-topic.

4. **Coherence and Cohesion:**
   - Assess the flow and organization of the essay.
   - Analyze how well the essay transitions between ideas and paragraphs.
   - Provide feedback on coherence and cohesion.

5. **Suggestions for Improvement:**
   - Offer specific recommendations to enhance the essay's quality, such as structuring, argumentation, or clarity.
   - Suggest areas where the writer can improve to reach a higher level of proficiency.
6. **strong points :**
   - please also mention strong points of the above eassy
   - and make all points with number 
7. **please also tell me the weaknesses of my eassy:**
   - i mean also explain some weak points of my eassy
   -and again make all points along with number counting 
8- **analyze with percentage :**
    - as we have covered four diffrent parameters if IELTS writing such as  (Grammar Mistakes,Lexical Resources,Task Response,Coherence and Cohesion)
    now you need to make the percentage of each i mean suppose we have 100% then analyze the all four deffrent parts along with percentage of each section


Please provide a concise evaluation of the IELTS essay for the following categories:
1. Grammar Mistakes
2. Lexical Resources
3. Task Response
4. Coherence and Cohesion
5. Suggestions for Improvement
6. strong points
7. please also tell me the weaknesses of my eassy
8. analyze with percentage 

Please ensure that the response includes detailed content under each of these sections. If the response still does not include the expected content, you may need to check your code and how you are extracting and presenting the response data from the OpenAI API.
and please make sure menstion all the above points.



"""
    
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompts,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        
        # Extract the generated feedback
        generated_feedback = response.choices[0].text

        # now i need to identify something 

        prompt_error=""" 

1. **Grammar Mistakes:**
   - Identify and list all grammatical errors present in the essay.
   - Create a table to organize these mistakes, with columns for the error type, sentence, and suggested correction.

2. **Lexical Resources:**
   - Identify any opportunities to use more advanced vocabulary and expressions.
   - Create a table with two columns: one for the words used by the user and the other for suggested vocabulary replacements.

3. **Task Response:**
   - Evaluate the essay's response to the essay prompt and task requirements.
   - Provide feedback on how well the essay addresses the task and stays on-topic.

4. **Coherence and Cohesion:**
   - Assess the flow and organization of the essay.
   - Analyze how well the essay transitions between ideas and paragraphs.
   - Provide feedback on coherence and cohesion.

5. **Suggestions for Improvement:**
   - Offer specific recommendations to enhance the essay's quality, such as structuring, argumentation, or clarity.
   - Suggest areas where the writer can improve to reach a higher level of proficiency.
6. **strong points :**
   - please also mention strong points of the above eassy
   - and make all points with number 
7. **please also tell me the weaknesses of my eassy:**
   - i mean also explain some weak points of my eassy
   -and again make all points along with number counting 
8- **analyze with percentage :**
    - as we have covered four diffrent parameters if IELTS writing such as  (Grammar Mistakes,Lexical Resources,Task Response,Coherence and Cohesion)
    now you need to make the percentage of each i mean suppose we have 100% then analyze the all four deffrent parts along with percentage of each section



        """

        print('---start----')
        print(generated_feedback)
        #now we need to break the generated_feedback into serval variables 
        sentence_dict=breaking_sentence(generated_feedback)
        print('-------end-------')
        print(sentence_dict)
        return sentence_dict
        
       
        

       


        
    except Exception as e:
        print("Error:", e)
        return None, None




from django.shortcuts import render, redirect
from .models import topics, Question

#this code is responsible for breaking entences into serval parts 
import re

def breaking_sentence(text):
    # Find indices of numbers followed by a period
    indices = [match.start() for match in re.finditer(r'\d+\.', text)]
    
    # Add the end of the text as the last index
    indices.append(len(text))
    
    sections_dict = {}
    # Split the text based on the indices found
    for i in range(len(indices) - 1):
        section_num = int(text[indices[i]:indices[i]+text[indices[i]:indices[i+1]].find('.')])
        sections_dict[section_num] = text[indices[i]:indices[i+1]].strip()
    
    return sections_dict

def test_code(request):
    return render(request,'chats.html')


def reading_content(request):
    return render(request,'reading_content.html')

def speaking_ai(request):
    return render(request,'index.html')
