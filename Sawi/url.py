from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

app_name = "Sawi"

urlpatterns = [
     url(r'^$', views.index, name="index"),
     url(r'^about/$', views.about, name="about"),
     url(r'^contactus/$', views.contactus, name="contact"),
     url(r'^courses/$', views.courses, name="courses"),
     url(r'^admission/$', views.admission, name="admission"),
     url(r'^gallery/$', views.gallery, name="gallery"),
     url(r'^formset/$', views.formsetView, name="formset"),
     url(r'^testpage/$', views.newSet, name="test"),
     url(r'^fileupload/$', views.uploadImages, name="test"),
     url(r'^news/(?P<title>)/$', views.index, name="news"),
     url(r'^login/$', views.loginView, name='Login'),
     #url(r'^login/$', auth_view.LoginView.as_view(template_name = "sawi/registration/login.html"), name='Login'),
    
    
    
    ]
