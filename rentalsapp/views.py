import requests
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

from rentalsapp.credentials import MpesaAccessToken, LipanaMpesaPassword
from rentalsapp.forms import ImageUploadForm
from rentalsapp.models import ImageModel,Agent,ContactModel


# Create your views here.

def home(request):
    images = ImageModel.objects.all()
    return render(request,'index.html',{'images':images})

def about(request):
    return render(request,'about.html')

def properties(request):
    images = ImageModel.objects.all()
    return render(request,'properties.html',{'images':images})

def services(request):
    return render(request,'services.html')

def agents(request):
    return render(request,'agents.html')

def starter(request):
    return render(request,'starter-page.html')
def agentregister(request):
    if request.method == 'POST':
        agent=Agent(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        agent.save()
        return redirect('/agentlogin')
    else:
        return render(request,'agent-register.html')

def agentlogin(request):
    if request.method == 'POST':
        if Agent.objects.filter(username=request.POST['username'],
                                password=request.POST['password']).exists():
            agent = Agent.objects.get(username=request.POST['username'],
                                      password=request.POST['password'],
            )
            return redirect('/houseuploads/',context={'agent':agent})
        else:
            return render(request,'agent-login.html')
    else:
        return render(request,'agent-login.html')

def showproperties(request):
    images = ImageModel.objects.all()
    return render(request,'show-properties.html',{'images':images})

def housedelete(request,id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showproperties')

def propertysingle(request):
    images = ImageModel.objects.all()
    return render(request,'property-single.html')

def houseedit(request,id):
    editimage = ImageModel.objects.get(id=id)
    return render(request,'house-edit.html',{'image':editimage})

def houseuploads(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showproperties')
    else:
        form = ImageUploadForm()
        return render(request,'house-uploads.html',{'form':form})

def houseupdate(request,id):
    updateinfo = ImageModel.objects.get(id=id)
    form = ImageUploadForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/showproperties')
    else:
        return render(request,'house-edit.html')

def searchhouse(request):
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')

    if query and category:
        houses = ImageModel.objects.filter(title__icontains=query, beds__iexact=category)
    else:
        houses = []
    return render(request,'search-result.html',{'houses':houses,'query':query,'category':category})

def contact(request):
    if request.method == "POST":
        mycontact=ContactModel(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

def pay(request):
    return render(request,'pay.html')

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Rentals",
            "TransactionDesc": "Life assurance"
        }
        response = requests.post(api_url, json=request, headers=headers)
        print(response.json())
        return HttpResponse("Success")


