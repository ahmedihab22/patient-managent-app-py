from django.shortcuts import render
from django.http import HttpResponse
from .models import patients
# Create your views here.

def home(request):
  return render(request,'commninfo/index.html')

def register(request):
    if request.method == 'POST':
     id = request.POST['id']
     username = request.POST['username']
     FirstName = request.POST['fname']
     LastName = request.POST['lname']
     Email = request.POST['email']
     password = request.POST['pass1']
     confpassword = request.POST['pass2']
    
     dateofbirth = request.POST['dob']

     if password != confpassword:
       return HttpResponse("password not matching")
     else:
       new_patient= patients (id=id,username=username ,FirstName=FirstName ,LastName=LastName ,Email=Email ,password=password ,confpassword=confpassword  ,dateofbirth=dateofbirth )
       new_patient.save()
       return HttpResponse('patient registered')
       
    return render (request,"commninfo/register.html")
    
def search(request):
  if request.method == 'POST':
   patient_id = request.POST.get('patient_id')
   try:
        patient_id= patients.objects.get(id=patient_id)
        return render (request,"commninfo/search.html",{'patient_id':patient_id})
   except patients.DoesNotExist:
        return render (request,"commninfo/search.html")
  
  return render (request,"commninfo/search.html")



def index(request):
  return render (request,"commninfo/index.html")