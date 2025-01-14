from django.contrib import admin
from django.urls import path
from Login import views

app_name="Login"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("signup/",views.Register,name="Register"),
    path("login/",views.loginpage,name="login"),
    path("",views.Dashboard,name="home"),
    path('waiting-email-verification/', views.waiting_email_verification, name='waiting-email-verification'), 
    path("portfolio/",views.portfolio,name="portfolio"),
    path("logout/",views.logoutuser,name="logout")
]