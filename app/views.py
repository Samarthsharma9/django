from django.shortcuts import redirect, render
from .models import Architect_table,Interior_Designer_table,Contractor_table, Contractor_table, Interior_Designer_table
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib import auth 

# Create your views here.

def home(request):
    return render (request, 'UI/DBpage1.html')

def Login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

    else:
        
        return render (request, 'Login/login.html')
    
    return render (request, 'login/login.html')

def Create_account(request):
        
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_address = request.POST['email_address']
        password = request.POST['password']
    
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email = email_address)
        user.save()
    
    else:
         return render (request, 'Login/login.html')
    
    return render (request, 'Login/login.html')


def Contractor(request):

    try:
        name = request.POST['name']
        Bio = request.POST['Bio']
        experience = request.POST['experience']
        fees = request.POST['fees']
    except MultiValueDictKeyError:
        name = False
        Bio = False 
        experience=False
        fees=False
        
        
    Contractor = Contractor_table(name=name, Bio=Bio, experience=experience,fees=fees)
    Contractor.save()
     #return redirect('/')

    return render (request, 'Contractor/index.html')

def Home_Design_Plan(request):
    return render (request, 'Home Design Plan/index.html')

def Construction_Material(request):
    return render (request, 'Construction Material/index.html')

def Architect(request):
    #comment
        try:
            name = request.POST['name']
            Bio = request.POST['Bio']
            experience = request.POST['experience']
        except MultiValueDictKeyError:
            name = False
            Bio = False 
            experience=False
        
        
        Architect = Architect_table(name=name, Bio=Bio, experience=experience)
        Architect.save()
        #return redirect('/')
                
        return render (request, 'Architect/index.html')

def Interior_Design(request):
    return render (request, 'Interior Design/index.html')

def Precast_Material(request):
    return render (request, 'Precast Material/index.html')

def Interior_Designer(request):

    try:
        name = request.POST['name']
        Bio = request.POST['Bio']
        experience = request.POST['experience']
        fees = request.POST['fees']
    except MultiValueDictKeyError:
        name = False
        Bio = False 
        experience=False
        fees=False
        
        
    Interior_Designer = Interior_Designer_table(name=name, Bio=Bio, experience=experience,fees=fees)
    Interior_Designer.save()
    #return redirect('/')

    return render (request, 'Interior Designer/index.html')
