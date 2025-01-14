from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth import get_backends
from allauth.account.utils import complete_signup
from django.contrib.auth.decorators import login_required
# Create your views here.

def Register(request):
    if request.method=="POST":
        form_data=request.POST
        print(form_data.get("password"),form_data.get("passwor2"))
        if form_data.get("password") != form_data.get("password2"):
            return render(request,"Login\Re.html",{"message":"Passwords that youz have entered does not match"})

        try:
            validate_password(form_data.get("password")) 
            user=User.objects.create(
                username=form_data.get("username"),
                email=form_data.get("email"),
                password=form_data.get("password")
            )
            user.save()
            success_url = redirect('Login:home').url
            complete_signup(request, user, success_url=success_url, signal_kwargs={},email_verification='mandatory')
            backend = get_backends()[0] 
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
                
                
            print(user)
            login(request,user)
            return redirect("Login:waiting-email-verification")
            
        except ValidationError as e:
            return render(request,"Login\Re.html",{"message":e})
        
        except IntegrityError as e:
            # Analyze the IntegrityError details for a specific message
            error_message = str(e)
            if "UNIQUE constraint failed" in error_message:
                return render(request, "Login/Re.html", {"message": "A user with this username or email already exists."})
            else:
                return render(request, "Login/Re.html", {"message": f"Database error: {error_message}"})
            
            
    return render(request ,"Login\Re.html")

def loginpage(request):
    if request.user.is_authenticated:
        return redirect("Login:home")
    if request.method=="POST":
        form_data=request.POST
        user=authenticate(request,username=form_data.get("username"),password=form_data.get("password"))
        print(user)
        if user is not None:
            login(request,user)
            return redirect("Login:home")
    return render(request,"Login\login.html")


@login_required(login_url="login/")
def Dashboard(request):
    if request.method=="POST":
        full_name = request.POST.get('full_name')
        professional_email = request.POST.get('professional_email', '')
        contact_number = request.POST.get('contact_number', '')
        professional_title = request.POST.get('professional_title', '')
        professional_narrative = request.POST.get('professional_narrative', '')
        education_level = request.POST.get('education_level', '')
        linkedin_profile = request.POST.get('linkedin_profile', '')
        github_portfolio = request.POST.get('github_portfolio', '')
        
        # Capture multiple work experiences (assuming dynamic form)
        work_experiences = []
        job_titles = request.POST.getlist('job_title')
        companies = request.POST.getlist('company')
        duration = request.POST.getlist('duration')
 
        job_descriptions = request.POST.getlist('job_description')
        
        for i in range(len(job_titles)):
            work_experiences.append({
                'job_title': job_titles[i],
                'company': companies[i],
                'duration': duration[i],
                'description': job_descriptions[i]
            })
        
        # Capture skills
        skills = request.POST.getlist('skill')
        
        # Prepare context for portfolio template
        context = {
            'full_name': full_name,
            'professional_title': professional_title,
            'professional_email': professional_email,
            'contact_number': contact_number,
            'professional_narrative': professional_narrative,
            'education_level': education_level,
            'work_experiences': work_experiences,
            'skills': skills,
            'linkedin_profile': linkedin_profile,
            'github_portfolio': github_portfolio
        }
        
        # Render portfolio template with context
        print(full_name)
        return render(request, 'Login\Portfolio.html', context)
    return render(request,'Login\dashboard.html')


def waiting_email_verification(request):
    return render(request, 'Login\waiting_email_verification.html')

# views.py
def portfolio(request):
    return render(request, 'Login/Portfolio.html')

@login_required(login_url="login/")
def logoutuser(request):
    logout(request)
    return redirect("Login:home")