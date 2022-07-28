from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('resume/', views.resume, name="resume"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    # path('/blog/<str:str>', views.blogPage, name="blogPage"),
]
