from django.shortcuts import render,get_object_or_404
from .models import ProfileGagan,EducationGagan,ProjectsGagan,ProjectPara,ProjectImage,Timeline,TechnicalStack,Hobbies

def home(request):
   query=ProfileGagan.objects.all()
   for k in query:
   	   projectcount=k.projectsgagan_set.all().count()
   	   pstack=k.technicalstack_set.all().count()
   return render(request,'Intro.html',{'query':query,'projectcount':projectcount,'pstack':pstack})

def timeline(request):
  query=ProfileGagan.objects.all()
  return render(request,'timeline.html',{'query':query})

def project(request,projectid):
  query=get_object_or_404(ProjectsGagan,id=projectid)
  return render(request,'projects.html',{'query':query})

def profile(request):
  query=ProfileGagan.objects.all()
  for k in query:
    projectcount=k.projectsgagan_set.all().count()
    pstack=k.technicalstack_set.all().count()
  return render(request,'profile.html',{"query":query,'projectcount':projectcount,'pstack':pstack})


def stack(request):
  query=ProfileGagan.objects.all()
  return render(request,'stack.html',{'query':query})

def viewpeoject(request):
  query=ProfileGagan.objects.all()
  return render(request,'post.html',{'query':query})
# Create your views here.
