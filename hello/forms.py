# from traceback import format_stack
import datetime
from django import forms
from hello.models import Scaffold, ScaffoldPosition

class AnmeldungForm(forms.ModelForm):
    class Meta:
        model = Scaffold
        
        fields = ("Description", "Area", "Installation","Equipment","Level","Geoposition", "Length", "Width", "Height", "Amount")
        widgets = {     
            'Description': forms.Textarea(attrs={'class':'form-control'}),       
            'Length': forms.NumberInput(attrs={'class':'form-control'}),
            'Width': forms.NumberInput(attrs={'class':'form-control'}),
            'Height': forms.NumberInput(attrs={'class':'form-control'}),
            'Amount': forms.NumberInput(attrs={'class':'form-control'}),          
            # 'Length': forms.Select(attrs={'class':'form-control col-sm'}),
            # 'Kunde': forms.Select(attrs={'class':'form-control'}),
            # 'Ansprechpartner': forms.Select(attrs={'class':'form-control'}),
            # 'Projekt': forms.Select(attrs={'class':'form-control'}),
            # 'Grund': forms.TextInput(attrs={'class':'form-control'}),
            # 'Anlage': forms.TextInput(attrs={'class':'form-control'}),
            # 'Ebene': forms.TextInput(attrs={'class':'form-control'}),
            # 'Oertlichkeit': forms.TextInput(attrs={'class':'form-control'}),
            # 'Aufbaudatum': forms.SelectDateWidget(attrs={'class':'form-control'}),
            # 'Abmeldedatum': forms.SelectDateWidget(attrs={'class':'form-control'})
        }
    Area = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Area').remote_field.model.objects.all(), empty_label="Bereich auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Bereich des Gerüstes", label="Bereich")
    Installation = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Installation').remote_field.model.objects.all(), empty_label="Anlage auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Anlage des Gerüstes", label="Bereich")
    Equipment = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Equipment').remote_field.model.objects.all(), empty_label="Equipment auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Equipment des Gerüstes", label="Equipment")
    Level = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Level').remote_field.model.objects.all(), empty_label="Ebene auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Ebene des Gerüstes", label="Bereich")
    Geoposition = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Geoposition').remote_field.model.objects.all(), empty_label="Örtlichkeit auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Örtlichkeit des Gerüstes", label="Örtlichkeit")
    SetupDate = forms.DateField(required=False, widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
    
class ScaffoldLogoutForm(forms.Form):
    scaffoldPositionChoice = forms.ModelChoiceField(queryset=ScaffoldPosition.objects.filter(Logout__isnull=True), empty_label="Gerüst zur Abmeldung auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Breich des Gerüstes", label="Gerüste") 
    LogoutDate = forms.DateField(required=False, initial=datetime.date.today().strftime('%Y-%m-%d'),  widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
    
