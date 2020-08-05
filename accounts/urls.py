
from django.urls import path, include
from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('signup', views.Siginup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),

]
