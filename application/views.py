from django.shortcuts import render


# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
   
    return render(request, 'index.html')