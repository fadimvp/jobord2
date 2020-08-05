from django.urls import path
from . import views
app_name='job'
urlpatterns = [

    path('contact-us',views.send_message,name='contact-us'),
]
