from django.urls import path
from temp_app import views

app_name= 'temp_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('others/', views.others, name='others'),
    
]

