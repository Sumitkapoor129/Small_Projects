from django.urls import path
from Home import views


app_name="Home"

urlpatterns=[path('',views.homepage,name="Homepage"),
path('login/',views.loginpage,name="login"),
path('register/',views.createuser,name="createuser")
# ,path('posts/',views.posts,name="posts")
]