from django.db import models

class ProfileGagan(models.Model):
	Name=models.CharField(max_length=100,default='Gagan Singh')
	Image=models.ImageField(upload_to='profilepic')
	Bio=models.CharField(max_length=10000,null=True)
	currently=models.CharField(max_length=100,blank=True)


class EducationGagan(models.Model):
	profilegagan=models.ForeignKey(ProfileGagan,on_delete=models.CASCADE)
	institute=models.CharField(max_length=500,blank=True)
	joiningperiod=models.CharField(max_length=150,blank=True)
	course=models.CharField(max_length=500,blank=True)
	date=models.DateTimeField(blank=True)
	score=models.CharField(max_length=10,blank=True)

	

class ProjectsGagan(models.Model):
	profilegagan=models.ForeignKey(ProfileGagan,on_delete=models.CASCADE)
	Name=models.CharField(max_length=100,blank=True)
	desc=models.CharField(max_length=1000,blank=True)
	Glink=models.CharField(max_length=200,blank=True,null=True)
	Llink=models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
		return self.Name

class ProjectPara(models.Model):
	projectsgagan=models.ForeignKey(ProjectsGagan,on_delete=models.CASCADE)
	paragraph=models.CharField(max_length=10000,blank=True)

class ProjectImage(models.Model):
	projectsgagan=models.ForeignKey(ProjectsGagan,on_delete=models.CASCADE)
	image=models.ImageField(upload_to='projectimage')

class Timeline(models.Model):
	profilegagan=models.ForeignKey(ProfileGagan,on_delete=models.CASCADE)
	dateof=models.DateTimeField(blank=True)
	heading=models.CharField(max_length=200,blank=True)
	bio=models.CharField(max_length=500,blank=True)


class TechnicalStack(models.Model):
	profilegagan=models.ForeignKey(ProfileGagan,on_delete=models.CASCADE)
	name=models.CharField(max_length=200,blank=True)
	image=models.ImageField(upload_to='technical_stack')
	desc=models.CharField(max_length=1000,blank=True)

	def __str__(self):
		return self.name

class Hobbies(models.Model):
	profilegagan=models.ForeignKey(ProfileGagan,on_delete=models.CASCADE)
	name=models.CharField(max_length=100,blank=True)


# Create your models here.
