from django.http import HttpResponse
import requests
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from googletrans import Translator
from .utils import translate
# Create your views here.

# USE USERNAME "SS" AND PASSWORD "SS"
def homepage(request):
    
    if request.method=="POST":
        if request.user.is_authenticated :
            text=request.POST.get("input")
            lang=request.POST.get("lang")
            T=translate(text,lang)
            context={"Translation":T}
            return render(request,'home.html',context)
        else:
            return redirect("Home:login")
        
    return render(request,'home.html')



def loginpage(request):
    if request.user.is_authenticated:
        return redirect("Home:Homepage")
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')   
        a=authenticate(request,username=username,password=password) 
        if a is not None:
            login(request,a)  
            return redirect("Home:Homepage")
    return render(request,'LoginPage1.html')



def createuser(request):
    if request.user.is_authenticated:
        return redirect("Home:Homepage")
    if request.method=="POST":
        user=User.objects.create_user(username=request.POST.get("username"),email=request.POST.get("email"),password=request.POST.get("password"))
        user.is_staff=True
        user.save()
        
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)  # Log the user in
            return redirect("Home:Homepage")
        else:
            return redirect("Home:Homepage")
    return render(request,"Register.html")

# def posts(request):
#     u="user@example.com"
#     p="string"
#     pl={"username":u,"password":p}
#     res=requests.post("http://127.0.0.1:8001/login",data=pl)
#     if res.status_code == 200:
#         token= res.json().get('access_token')
#         headers = {"Authorization": f"Bearer {token}"}
#         res= requests.get("http://127.0.0.1:8001/post", headers=headers)
#         result=res.json()
#     else:
#         result="Error"
    
#     print(result)
#     return render(request,'posts.html',{"posts":result})