# from traceback import format_stack
from django import forms
from hello.models import LogMessage, Scaffold

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message", "name")
        
class LogMessageForm2(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message", "name", "source")

class AnmeldungForm(forms.ModelForm):
    class Meta:
        model = Scaffold
        fields = ("Area", "Installation","Equipment","Level","Geoposition", "Length", "Width", "Height", "Amount")
        widgets = {            
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
    Area = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Area').remote_field.model.objects.all(), empty_label="Bereich auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Breich des Gerüstes", label="Bereich")
    Installation = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Installation').remote_field.model.objects.all(), empty_label="Anlage auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Anlage des Gerüstes", label="Bereich")
    Equipment = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Equipment').remote_field.model.objects.all(), empty_label="Equipment auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Equipment des Gerüstes", label="Equipment")
    Level = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Level').remote_field.model.objects.all(), empty_label="Ebene auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Ebene des Gerüstes", label="Bereich")
    Geoposition = forms.ModelChoiceField(queryset=Scaffold._meta.get_field('Geoposition').remote_field.model.objects.all(), empty_label="Örtlichkeit auswählen..", widget=forms.Select(attrs={'class':'form-control'}), help_text="Örtlichkeit des Gerüstes", label="Bereich")
  
    #     # Plan Data
    # Length= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Länge')
    # Width= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Breite')
    # Height= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Höhe')
    # Amount= models.DecimalField(max_digits= 4, decimal_places= 0, blank= True, null= True, verbose_name= 'Plan Anzahl')
        
    """ #         # PK
    # Geruestnummer= models.AutoField(primary_key= True, help_text="Die Gerüstnummer wird automatisch erzeugt.")
    
    # FK
    Kunde= models.ForeignKey(Firma, on_delete=models.PROTECT, verbose_name= 'Firma')
    Ansprechpartner= models.ForeignKey(Ansprechpartner, on_delete=models.PROTECT, verbose_name= 'Ansprechpartner')
    Projekt = models.ForeignKey(Projekt, on_delete=models.PROTECT, verbose_name= 'Projekt Name')
    
    Grund= models.TextField(blank= True, verbose_name= 'Grund', help_text="Kurze Begründung warum das Gerüst angefordert wird.")
    Anlage= models.CharField(max_length= 100, blank= True, verbose_name= 'Anlage/ Equipment')
    Ebene= models.CharField(max_length= 100, blank= True, verbose_name= 'Ebene')
    Oertlichkeit= models.CharField(max_length= 100, blank= True, verbose_name= 'Oertlichkeit')

    #Dates
    Eingangsdatum= models.DateField(default = timezone.now, verbose_name= 'Eingangsdatum')
    Aufbaudatum = models.DateField(blank = True, null = True, verbose_name= 'Aufbaudatum')
    Abmeldedatum = models.DateField(blank = True, null = True, verbose_name= 'Abmeldedatum')

    #Renting
    Mietbeginn= models.DateField(blank= True, null= True, verbose_name= 'Miet-Beginn')
    Mietende= models.DateField(blank= True, null= True, verbose_name= 'Miet-Ende')

    #Price
    Preis= models.DecimalField(max_digits= 12, decimal_places= 2, blank= True, null= True, verbose_name= 'Preis')

    class Meta:
        verbose_name_plural= 'Geruestbuch' """