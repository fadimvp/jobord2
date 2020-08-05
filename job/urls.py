from django.urls import path
from . import views
from . import api
app_name='job'
urlpatterns = [
    path('',views.Job_List,name='job_list'),
    path('add',views.addjob,name='addjob'),
    path('api/list',api.joblistapi,name='jobapi'),
    path('api/jobs_d/<int:id>',api.job_detial_api,name='job_detial_api'),
    path('<str:slug>/',views.jo_detail,name='job_d'),
]
