# import re
# from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime

from django.shortcuts import redirect
from hello.forms import LogMessageForm, LogMessageForm2, AnmeldungForm
from hello.models import LogMessage, ScaffoldPosition, AdditionalServices

from django.views.generic import ListView

def testModelHandling(request):
    context = {}
    context['datalist'] = ScaffoldPosition.objects.all()
    return render(request, "hello/test.html", context)
    

def runOldVersion(request):
    # return render(request, "hello/index.html")
    context = {}
    context['datalist'] = ScaffoldPosition.objects.all()
    context['additionalServices']=AdditionalServices.objects.all()
    if request.method == "POST":
        form = AnmeldungForm(request.POST)
        if form.is_valid():            
            results = form.save()
            newScaffoldPosition = ScaffoldPosition()
            newScaffoldPosition.Scaffold = results
            newScaffoldPosition.Version = 0
            newScaffoldPosition.Type = 1
            newScaffoldPosition.save()            
    context['formAnmeldung'] = AnmeldungForm()
    return render(request, "hello/index.html", context)

    # Version= models.DecimalField(max_digits= 4, decimal_places= 0, blank= True, null= True, verbose_name = 'Gerüstversion')
    
    # # Data
    # Type=models.CharField(max_length=12, choices=SCAFFOLD_POSITION_TYPES, blank = True)
    # RegistrationDate=models.DateField(default = timezone.now, verbose_name= 'Anmeldedatum')
    # SetupDate=models.DateField(default = timezone.now, verbose_name= 'Aufbaudatum', blank = True)
    # Logout=models.DateField(default = timezone.now, verbose_name= 'Abmeldedatum', blank = True)
        
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

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
    
# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)
    form2 = LogMessageForm2(request.POST or None)

    if request.method == "POST":
        submitted_form_name = request.POST.get('submit_button')
        if submitted_form_name == 'submit_form1':
            if form.is_valid():
                message = form.save(commit=False)
                message.log_date = datetime.now()
                message.source = "A"
                message.save()
                return redirect("home")
        elif submitted_form_name == 'submit_form2':
            if form2.is_valid():
                message = form2.save(commit=False)
                message.log_date = datetime.now()
                message.source = "B"
                message.save()
                return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form, "form2": form2})