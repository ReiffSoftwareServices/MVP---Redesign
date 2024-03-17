from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("", views.registerScaffold, name="mvp"),
    path("test/", views.testModelHandling, name="testModelHandling"),
    path("mail/", views.testMail, name = "testMail"),    
]

urlpatterns += staticfiles_urlpatterns()