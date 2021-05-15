from django.shortcuts import render
from .models import Projects
from django.http import HttpResponse
# Create your views here.

def project_list(request):
	# return HttpResponse("Hello world")
	project = Projects.objects.all()
	return render(request,'projects/project.html',{'projects':project})