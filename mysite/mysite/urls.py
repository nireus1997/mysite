"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# from blog import views as MainView
from blog import WebSecView
from blog import HomeView, FuzzView, BlogView, NewsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',HomePageView.ShowIndex),

    # websec page
    url(r'^$',WebSecView.ShowMainPage, name="ShowMainPage"),

    url(r'^websec/$',WebSecView.Show_WebSecPage_by_Cat, name="Show_WebSecPage_by_Cat"),
    url(r'^websec/([0-9]+)/$',WebSecView.Show_WebSecPage_blog_detail, name="Show_WebSecPage_blog_detail"),

    url(r'^home/$', HomeView.ShowAbout, name="Show_About"),

    url(r'^fuzz/$', FuzzView.ShowAbout, name="Show_About"),

    url(r'^blog/$', BlogView.ShowAbout, name="Show_About"),

    url(r'^news/$', NewsView.ShowAbout, name="Show_About"),
]
