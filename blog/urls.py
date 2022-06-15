from django.urls import path
from . import views
domains = views.Domains()
urlpatterns = [
    path('',domains.index, name="home"),
    path('index',domains.index),
    path('blogs',domains.blogs,name="blogs"),
    path('blogs/<int:id>',domains.blog_details,name="blog_details"),
    path('login',domains.login , name="login")
]
