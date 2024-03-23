# import re
# from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime
from django.utils import timezone

from django.shortcuts import redirect
from hello.forms import AnmeldungForm, ScaffoldLogoutForm, checkForm
from hello.models import ScaffoldPosition, AdditionalServices, CostPosition, Contact

from django.views.generic import ListView

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

def aufmass(request, scaffoldID):
    context = {}
    context['scaffoldID'] = scaffoldID
    context['formCheck'] = checkForm()
    return render(request,'hello/test.html', context)
       
def testModelHandling(request):
    context = {}
    context['datalist'] = ScaffoldPosition.objects.all()
    return render(request, "hello/test.html", context)
    
def testMail(request):
    message = "testmessage"
    email = "jan.j.reiff@gmail.com"
    name = "Jan Reiff"
    send_mail(
        name,
        message,
        'settings.EMAIL_HOST_USER',
        [email],
        fail_silently=False
    )
    return HttpResponseRedirect(reverse('mvp'))
    
def registerScaffold(request):
    # return render(request, "hello/index.html")
    context = {}
    context['datalist'] = ScaffoldPosition.objects.all()
    context['additionalServices']=AdditionalServices.objects.all()
    context['today']=timezone.now()
    if request.method == "POST":
        if 'registerScaffold' in request.POST:
            print('register')
            form = AnmeldungForm(request.POST)
            if form.is_valid():            
                results = form.save()
                additionalServicesSelected = request.POST.getlist('additionalServiceSelection')
                newScaffoldPosition = ScaffoldPosition()
                newScaffoldPosition.Scaffold = results
                newScaffoldPosition.Version = 0
                newScaffoldPosition.Type = 1
                newScaffoldPosition.save()
                newScaffoldPosition.SetupDate = request.POST.get('SetupDate')
                if newScaffoldPosition.SetupDate == "" :
                    newScaffoldPosition.SetupDate = None
                newScaffoldPosition.Logout =  None
                for additionalServiceChoice in additionalServicesSelected:
                    print(additionalServiceChoice)
                    targetItem = AdditionalServices.objects.get(id=additionalServiceChoice)
                    newScaffoldPosition.AdditionalServices.add(targetItem)
                newScaffoldPosition.save()
                message = "Es wurde ein neues Gerüst angemeldet. Bla bla. Hier bitte Aufmaß eingeben: " + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + reverse('aufmass',args=[newScaffoldPosition.Scaffold.ScaffoldID])
                message = message.replace("//", "/")
                email = "jan.j.reiff@gmail.com"
                name = "Neue Gerüstanmeldung!"
                send_mail(
                    name,
                    message,
                    'settings.EMAIL_HOST_USER',
                    [email,'christoph.lehnertz@web.de'],
                    fail_silently=False
                )  
        elif 'logutScaffold' in request.POST:
            form = ScaffoldLogoutForm(request.POST)
            scaffoldToLogout = request.POST.get('scaffoldPositionChoice')
            # ToDo: Hier das Gerüst abmelden
            targetScaffoldPosition = ScaffoldPosition.objects.get(id=scaffoldToLogout)
            targetScaffoldPosition.Logout = request.POST.get('LogoutDate')
            targetContactId = request.POST.get('contactLogout') 
            targetScaffoldPosition.LogoutContact = Contact.objects.get(id=targetContactId)
            targetScaffoldPosition.save()
        elif 'checkScaffold' in request.POST:
            form_data = request.POST
            selectedScaffold = form_data.get('scaffoldPositionChoice')
            print(selectedScaffold)
            valuesSelected = form_data.getlist('costPositions')
            for name in valuesSelected:
                print(name)
        
                  
    context['formAnmeldung'] = AnmeldungForm()
    context['formScaffoldLogout'] = ScaffoldLogoutForm()
    context['formCheck'] = checkForm()
    return render(request, "hello/index.html", context)
        
def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(
        request,
        'hello/hello_there.html',
        {
            'name' : name, 
            'date': datetime.now()
        }
    )
    
# # Add this code elsewhere in the file:
# def log_message(request):
#     form = LogMessageForm(request.POST or None)
#     form2 = LogMessageForm2(request.POST or None)

#     if request.method == "POST":
#         submitted_form_name = request.POST.get('submit_button')
#         if submitted_form_name == 'submit_form1':
#             if form.is_valid():
#                 message = form.save(commit=False)
#                 message.log_date = datetime.now()
#                 message.source = "A"
#                 message.save()
#                 return redirect("home")
#         elif submitted_form_name == 'submit_form2':
#             if form2.is_valid():
#                 message = form2.save(commit=False)
#                 message.log_date = datetime.now()
#                 message.source = "B"
#                 message.save()
#                 return redirect("home")
#     else:
#         return render(request, "hello/log_message.html", {"form": form, "form2": form2})