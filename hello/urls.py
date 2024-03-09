from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("", views.runOldVersion, name="mvp"),
    path("test/", views.testModelHandling, name="testModelHandling"),
    
    
]

urlpatterns += staticfiles_urlpatterns()