# import re
# from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime
from django.utils import timezone

from django.shortcuts import redirect
from hello.forms import AnmeldungForm, ScaffoldLogoutForm, checkForm
from hello.models import ScaffoldPosition, AdditionalServices, CostPosition

from django.views.generic import ListView

def testModelHandling(request):
    context = {}
    context['datalist'] = ScaffoldPosition.objects.all()
    return render(request, "hello/test.html", context)
    

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
        elif 'logutScaffold' in request.POST:
            form = ScaffoldLogoutForm(request.POST)
            scaffoldToLogout = request.POST.get('scaffoldPositionChoice')
            # ToDo: Hier das Gerüst abmelden
            targetScaffoldPosition = ScaffoldPosition.objects.get(id=scaffoldToLogout)
            targetScaffoldPosition.Logout = request.POST.get('LogoutDate')
            targetScaffoldPosition.save()
        
                  
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