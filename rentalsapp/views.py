from django.shortcuts import render, redirect
from rentalsapp.forms import ImageUploadForm
from rentalsapp.models import ImageModel


# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def properties(request):
    return render(request,'properties.html')

def services(request):
    return render(request,'services.html')

def agents(request):
    return render(request,'agents.html')

def starter(request):
    return render(request,'starter-page.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')

def agentlogin(request):
    return render(request,'agent-login.html')
def agentadmin(request):
    return render(request,'agent-admin.html')
def houseuploads(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showproperties')
    else:
        form = ImageUploadForm()
    return render(request,'house-uploads.html',{'form':form})
def showproperties(request):
    images = ImageModel.objects.all()
    return render(request,'show-properties.html',{'property':images})