from django.urls import path
from . import views

urlpatterns = [
    path('', views.speaking),
    path('success',views.store_feedback),
    path('essay/<int:essay_id>', views.essay_detail),


]
