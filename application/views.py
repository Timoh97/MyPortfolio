from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Project


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
   
    return render(request, 'index.html')

def biodata(request):
   
    return render(request, 'biodata.html')

def profile(request):
  
  
  return render(request, 'profile.html')



def project(request):
  
    project = Project.objects.all()
    context={
        
        'project' : project,
    }
    return render(request, 'project.html', context)