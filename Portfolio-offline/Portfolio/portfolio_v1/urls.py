from django.urls import path, re_path

from portfolio_v1 import views


urlpatterns = [ 
            path("",views.base,name = "index"),
            path("about",views.about,name= "about"),
            path("test",views.test),
            path("contact",views.contact),
        
               ]

