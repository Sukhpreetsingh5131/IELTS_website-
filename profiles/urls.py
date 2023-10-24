from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.thankyou),
    path('writing/community/', views.writing),
    path('writing/ai',views.writing_ai),
    path('writing/ai/check', views.evaluate_writing),
    path('speaking/liveroom/',views.speaking),
    path('speaking/ai',views.speaking_ai),
    path('reading/news',views.reading),
    path('otp/',views.send_otp),
    
    path('param/',views.param),
    
    path('otp_check/',views.otp_check),
    path('home_page/',views.register_user),
    path('resend/otp/',views.resend_otp),
    path('submited', views.submit_basic_info),
    path('reading/content',views.reading_content),
   
    
    path('chat_app/',views.chats),
    path('test/',views.test_code),
   
 
    path('community/',views.community),
    path('room_app/create/<int:room_id>/', views.room_opens),
]

    
   






