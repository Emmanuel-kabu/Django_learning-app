from django.urls import path
from . import views
app_name = 'MylearningApp'

urlpatterns = [
 path('', views.index, name = 'index'),
 path('course/', views.course, name = 'course'),
 path('faq/', views.faq, name = 'faq'),
 path('about/', views.about, name = 'about'),
 path('privacy/', views.privacy, name ='privacy'),
 path('support/', views.support, name = 'support'),
 path('t_and_c/', views.t_and_c, name = 't_and_c'),
 path('community/', views.community, name='community'),
 path('testimonials/', views.testimonials, name='testimonials'),                                                       
 path('profile/', views.profile, name='profile'),
 path('notification/', views.notification, name = 'notification'),
 path('home/', views.home , name = 'home')

 

]
