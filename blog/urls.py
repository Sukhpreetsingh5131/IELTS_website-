from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.first_page),

    path('<int:id>',views.detail_info,name='book-detail'),
    path('posts/',views.blogs_open),
    
    path('posts/home',views.post_home),
    path('posts/abouts',views.about),
    path('posts/studentdata',views.post_student),

    path('posts/form',views.reviews),
    path('posts/teacher',views.teacher),

    path('thankyou',views.guru),
    
    #path('posts/<slug:slug>',views.blog_information)
]



