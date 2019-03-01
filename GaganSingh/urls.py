from django.urls import path
from GaganSingh import views

urlpatterns=[
  path('',views.home,name='home'),
  path('timeline',views.timeline,name='timeline'),
  path('Projects/<int:projectid>',views.project,name='project'),
  path('Projects/',views.viewpeoject,name='finalproject'),
  path('Profile',views.profile,name='profile'),
  path('stack',views.stack,name='stack'),
  ]