from django.db import models
from datetime import date
from django.utils import timezone

class Contact(models.Model):
    Prename= models.CharField(max_length = 50, blank = True, verbose_name = 'Vorname')
    Surname= models.CharField(max_length = 50, blank = True,  verbose_name = 'Nachname')
    Email= models.EmailField(max_length =254, blank = True, verbose_name = 'Email')
    
    class Meta:
        verbose_name_plural= 'Kontaktliste'

    def __str__(self):
        return '{} {}'.format(self.Prename, self.Surname)
    
class Area(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Bereich')
    Contact= models.ForeignKey(Contact, on_delete=models.CASCADE, blank = True, verbose_name= 'Ansprechpartner')
    
    class Meta:
        verbose_name_plural= 'Bereiche'
        
    def __str__(self):
        return '{} ({} {})'.format(self.Name, self.Contact.Prename, self.Contact.Surname)

class Installation(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Anlage')
    
    class Meta:
        verbose_name_plural= 'Anlagen'
    def __str__(self):
            return '{}'.format(self.Name)
        
class Equipment(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Equipment')
    
    class Meta:
        verbose_name_plural= 'Equipments'
    
    def __str__(self):
            return '{}'.format(self.Name)
        
class Level(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Ebene')
    
    class Meta:
        verbose_name_plural= 'Ebenen'

    def __str__(self):
            return '{}'.format(self.Name)
        
class Geoposition(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Örtlichkeit')
    
    class Meta:
        verbose_name_plural= 'Örtlichkeiten'
    
    def __str__(self):
            return '{}'.format(self.Name)

class extraInfo1(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Bauteil')
    
    class Meta:
        verbose_name_plural= 'Bauteile'
    
    def __str__(self):
            return '{}'.format(self.Name)
        
class extraInfo2(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Koordinaten')
    
    class Meta:
        verbose_name_plural= 'Koordinaten'
    
    def __str__(self):
            return '{}'.format(self.Name)

class extraInfo3(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Innengerüst')
    
    class Meta:
        verbose_name_plural= 'Innengerüste'
    
    def __str__(self):
            return '{}'.format(self.Name)
                
class Scaffold(models.Model):
    # PK
    ScaffoldID= models.AutoField(primary_key= True, help_text="Die Gerüstnummer wird automatisch erzeugt.")
    Description= models.TextField(blank= True, null= True, verbose_name= 'Beschreibung', help_text="Füge hier beliebige Notizen hinzu.")
    # FK
    Area= models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name= 'Bereich', blank= True, null= True, help_text="Bereich.")
    Installation= models.ForeignKey(Installation, on_delete=models.CASCADE, verbose_name= 'Anlage', blank= True, null= True, help_text="Anlage.")
    Equipment= models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name= 'Equipment', blank= True, null= True, help_text="Equipment.")
    Level= models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name= 'Ebene', blank= True, null= True, help_text="Level")
    Geoposition= models.ForeignKey(Geoposition, on_delete=models.CASCADE, blank= True, null= True, verbose_name= 'Örtlichkeit', help_text="Örtlichkeit")
    extraInfo1= models.ForeignKey(extraInfo1, on_delete=models.CASCADE, blank= True, null= True, verbose_name= 'Bauteil', help_text="Bauteil")
    extraInfo2= models.ForeignKey(extraInfo2, on_delete=models.CASCADE, blank= True, null= True, verbose_name= 'Koordinaten', help_text="Koordinaten")
    extraInfo3= models.ForeignKey(extraInfo3, on_delete=models.CASCADE, blank= True, null= True, verbose_name= 'Innengerüst', help_text="Innengerüst")
    
    # Plan Data
    Length= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Länge', help_text="Länge in m")
    Width= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Breite', help_text="Breite in m")
    Height= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Höhe', help_text="Höhe in m")
    Amount= models.DecimalField(max_digits= 4, decimal_places= 0, blank= True, null= True, verbose_name= 'Plan Anzahl', help_text="Anzahl der Gerüste")
    
    class Meta:
        verbose_name_plural= 'Gerüste'
        
    def __str__(self):
            return '({}) - {} | {} | {} | {} : L{}B{}H{}x{}'.format(self.ScaffoldID, self.Area, self.Installation, self.Equipment, self.Geoposition, self.Length, self.Width, self.Height, self.Amount)
     
class AdditionalServices(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Zusatzleistung')

    class Meta:
        verbose_name_plural= 'Zusatzleistungen'
    
    def __str__(self):
            return '{}'.format(self.Name)
        
SCAFFOLD_POSITION_TYPES = {
    "1":"Anmeldung",
    "2":"Erweiterung"
}        
  
class ScaffoldPosition(models.Model):
    #PK
    Scaffold= models.ForeignKey(Scaffold, on_delete=models.CASCADE, blank = True, verbose_name= 'Geruest')
    Version= models.DecimalField(max_digits= 4, decimal_places= 0, blank= True, null= True, verbose_name = 'Gerüstversion')
    
    # Data
    Type=models.CharField(max_length=12, choices=SCAFFOLD_POSITION_TYPES, blank = True)
    RegistrationDate=models.DateField(default = timezone.now, verbose_name= 'Anmeldedatum')
    SetupDate=models.DateField(default = timezone.now, verbose_name= 'Aufbaudatum', blank = True, null= True)
    Logout=models.DateField(default = timezone.now, verbose_name= 'Abmeldedatum', blank = True, null= True)
    LogoutContact= models.ForeignKey(Contact, on_delete=models.CASCADE, blank = True, null= True, verbose_name= 'Abmelder')
    
    # Additional Services
    AdditionalServices = models.ManyToManyField(AdditionalServices, blank = True)
    
    
    class Meta:
        verbose_name_plural= 'Gerüstpositionen'
    
    def __str__(self):
            return '{}.{} - {}'.format(self.Scaffold.ScaffoldID, self.Version, SCAFFOLD_POSITION_TYPES[self.Type])   

    @property
    def TypeString(self):
        return SCAFFOLD_POSITION_TYPES[self.Type]
    
COSTPOSITION_MEASURE_TYPES = {
    "1":"h",
    "2":"m",
    "3":"m²",
    "4":"m³"
}  
        
class CostPosition(models.Model):
    Name= models.CharField(max_length = 50, verbose_name = 'Leistungsposition')
    Measure= models.CharField(max_length = 2, verbose_name = 'Einheit', choices=COSTPOSITION_MEASURE_TYPES)
    Price= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name = 'Preis pro Einheit in €')
    
    class Meta:
        verbose_name_plural= 'Leistungsverzeichnis'
    
    def __str__(self):
            return '{} in {} für {}€'.format(self.Name, COSTPOSITION_MEASURE_TYPES[self.Measure], self.Price)
        
class ChosenCostPosition(models.Model):
    ScaffoldPosition= models.ForeignKey(ScaffoldPosition, on_delete=models.CASCADE, blank = True, null=True, verbose_name= 'Gerüstversion')
    CostPosition= models.ForeignKey(CostPosition, on_delete=models.CASCADE, blank = True, null=True, verbose_name= 'Leistungsposition')
    
    
    TargetLength= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Länge')
    TargetWidth= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Breite')
    TargetHeight= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Plan Höhe')
    TargetAmount= models.DecimalField(max_digits= 4, decimal_places= 0, blank= True, null= True, verbose_name= 'Plan Anzahl')
    TargetHours= models.DecimalField(max_digits= 4, decimal_places= 0, blank= True, null= True, verbose_name= 'Plan Stunden')
    
    Length= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'IST Länge', help_text="Länge")
    Width= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'IST Breite', help_text="Breite")
    Height= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'IST Höhe', help_text="Höhe")
    Amount= models.DecimalField(max_digits= 4, decimal_places= 0, blank= True, null= True, verbose_name= 'IST Anzahl')
    Hours= models.DecimalField(max_digits= 4, decimal_places= 0, blank= True, null= True, verbose_name= 'IST Stunden')
    
    Requested= models.BooleanField(default=False, verbose_name= 'ist freigegeben')
    Confirmed= models.BooleanField(default=False, verbose_name= 'ist bestätigt')
    
    class Meta:
        verbose_name_plural= 'Leistungspositionen'

    def __str__(self):
            return '{}'.format(self.CostPosition)
        











# # Create your models here.
# class LogMessage(models.Model):
#     message = models.CharField(max_length=300, blank=True, null=True, help_text="xxx")
#     name = models.CharField(max_length=100, blank=True, null=True, help_text="yyy")
#     source = models.CharField(max_length=2, blank=True, null=True, help_text="yyx")
#     log_date = models.DateTimeField("date logged", blank=True, null=True, help_text="yxcv")
    
#     def __str__(self):
#         date = timezone.localtime(self.log_date)
#         return f"'{self.message}' logged {date.strftime('%A, %d %B, %Y at %X')}"
   
# class Firma(models.Model):
#     Name= models.CharField(max_length= 100, blank= False, verbose_name= 'Firma')
#     Postleitzahl= models.CharField(max_length= 8, blank = True, verbose_name = 'Postleitzahl')
#     Stadt= models.CharField(max_length= 30, blank = True, verbose_name = 'Stadt')
#     Strasse= models.CharField(max_length= 30, blank = True, verbose_name = 'Strasse')
#     Email= models.EmailField(max_length = 254, blank= True, verbose_name = 'Firma Email')
#     Telefon= models.CharField(max_length= 30, blank = True, verbose_name = 'Telefon Firma')
    
#     class Meta:
#         verbose_name_plural= 'Firmenliste'
        
#     def __str__(self):
#         return '{}'.format(self.Name)

# class Ansprechpartner(models.Model):
#     Nachname= models.CharField(max_length = 50, blank = True,  verbose_name = 'Nachname')
#     Vorname= models.CharField(max_length = 50, blank = True, verbose_name = 'Vorname')
#     Email= models.EmailField(max_length =254, blank = True, verbose_name = 'Email Ansprechpartner')
#     Telefon= models.CharField(max_length = 20, blank = True, verbose_name = 'Telefon Ansprechpartner')
#     Firma= models.ForeignKey(Firma, on_delete=models.PROTECT, verbose_name= 'Firma')

#     class Meta:
#         verbose_name_plural = 'Ansprechpartner'

#     def __str__(self):
#         return  '{}, {}'.format(self.Nachname, self.Vorname)

# class Inventar(models.Model):

#     Name = models.CharField(max_length = 50, verbose_name= 'Bauteil')
#     Einheit= models.CharField(max_length= 50, verbose_name= 'Einheit')
#     Beschreibung = models.TextField(blank = True, verbose_name = 'Beschreibung')
#     Preis = models.DecimalField(max_digits = 7, decimal_places = 2, blank = True, null = True, verbose_name= 'Preis') ## Not sure whether they can be zero!

#     # Miete
#     Einheit_Miete= models.CharField(max_length= 50, verbose_name= 'Einheit Miete')
#     Beschreibung_Miete= models.CharField(max_length= 50, verbose_name= 'Beschreibung Miete')
#     Preis_Miete= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Preis Miete')


#     class Meta:
#         verbose_name_plural= 'Leistungsverzeichnis'

#     def __str__(self):
#         return '{}'.format(self.Name)   
    
# class Projekt(models.Model):

#     ''' Table just for creating the project name '''

#     Project_Name= models.CharField(max_length= 50, primary_key= True, verbose_name= 'Projekt Name')

#     class Meta:
#         verbose_name_plural= 'Projekte'

#     def __str__(self):
#         return '{}'.format(self.Project_Name)

# class Geruestbuch(models.Model):
#     # PK
#     Geruestnummer= models.AutoField(primary_key= True, help_text="Die Gerüstnummer wird automatisch erzeugt.")
    
#     # FK
#     Kunde= models.ForeignKey(Firma, on_delete=models.PROTECT, verbose_name= 'Firma')
#     Ansprechpartner= models.ForeignKey(Ansprechpartner, on_delete=models.PROTECT, verbose_name= 'Ansprechpartner')
#     Projekt = models.ForeignKey(Projekt, on_delete=models.PROTECT, verbose_name= 'Projekt Name')
    
#     Grund= models.TextField(blank= True, verbose_name= 'Grund', help_text="Kurze Begründung warum das Gerüst angefordert wird.")
#     Anlage= models.CharField(max_length= 100, blank= True, verbose_name= 'Anlage/ Equipment')
#     Ebene= models.CharField(max_length= 100, blank= True, verbose_name= 'Ebene')
#     Oertlichkeit= models.CharField(max_length= 100, blank= True, verbose_name= 'Oertlichkeit')

#     #Dates
#     Eingangsdatum= models.DateField(default = timezone.now, verbose_name= 'Eingangsdatum')
#     Aufbaudatum = models.DateField(blank = True, null = True, verbose_name= 'Aufbaudatum')
#     Abmeldedatum = models.DateField(blank = True, null = True, verbose_name= 'Abmeldedatum')

#     #Renting
#     Mietbeginn= models.DateField(blank= True, null= True, verbose_name= 'Miet-Beginn')
#     Mietende= models.DateField(blank= True, null= True, verbose_name= 'Miet-Ende')

#     #Price
#     Preis= models.DecimalField(max_digits= 12, decimal_places= 2, blank= True, null= True, verbose_name= 'Preis')

#     class Meta:
#         verbose_name_plural= 'Geruestbuch'


#     def __str__(self):
#         return '{} - Gerüst {}'.format(self.Projekt, self.Geruestnummer) 
    
#     @property
#     def Mietwochen(self):
#         if (self.Aufbaudatum is not None) and (self.Abmeldedatum is not None):
#             time_diff= (self.Abmeldedatum- self.Aufbaudatum).days
#             return int(round(time_diff/ 7)- 6)                                     # Set to six weeks now
#         else:
#             return None


#     # Get the status of the Project
#     @property
#     def Status(self):
#         if (self.Abmeldedatum is not None) and (self.Abmeldedatum < date.today()):
#             return 'Abgeschlossen'
#         else:
#             return 'Laufend'
#     def save(self, *args, **kwargs):
#         '''Calculating the price per Geruestnummer'''
#         #1. Getting all equipment from geruestnummer and the corresponding prices.
#         query= Equipments.objects.filter(Geruestnummer= self.Geruestnummer).values_list('Equipment' ,flat= True)    #Output= <QuerySet [1, 2, 1, 2]>, which represents the equipment_id per geruestnummer
#         preise= []
#         for i in query:
#             preise.append(Inventar.objects.filter(id= i).values_list('Preis', flat= True)[0])

#         #2. Getting the amount per equipment
#         query= Equipments.objects.filter(Geruestnummer= self.Geruestnummer).values_list('Laenge', 'Breite', 'Hoehe', 'Stueck', 'Stunde')
#         amount= []
#         for i in query:
#             if (i[0] is not None) and (i[1] is not None) and (i[2] is not None):  #Laenge* Breite* Hoehe
#                 amount.append(i[0]* i[1]* i[2])
#             elif ((i[3] is not None) and (i[4] is not None)): #Not sure whether this is required!
#                 amount.append(i[3]* i[4])
#             else:
#                 amount.append(0)
#         #3. amount= (1,2), preise= (2,3). Elementwise multipilication of the two lists. If None a zero is assigned!
#         output= []
#         for i in range(len(amount)):
#             if (amount[i] is not None) and (preise[i] is not None):
#                 output.append(amount[i]* preise[i])
#             else:
#                 output.append(0)
#         output= sum(output)

#         self.Preis= output
#         super(Geruestbuch, self).save(*args, **kwargs)

#     @property
#     def Miete():
#         pass

# class Equipments(models.Model):

#     '''
#     Equipment per Geruestnummer
#     '''
       
#     # FK
#     Geruestnummer= models.ForeignKey(Geruestbuch, on_delete=models.PROTECT, verbose_name= 'Geruestnummer')
#     Equipment= models.ForeignKey(Inventar, on_delete=models.PROTECT, verbose_name= 'Inventar')

#     #Metrics
#     Laenge= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Laenge')
#     Breite= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Breite')
#     Hoehe= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Hoehe')
#     Stueck= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Stueck')
#     Stunde= models.DecimalField(max_digits= 7, decimal_places= 2, blank= True, null= True, verbose_name= 'Stunde')


#     class Meta:
#         verbose_name_plural= 'Equipment'
        
#         def __str__(self):
#             return '{} - {} - {} Stk. {}x{}x{} ({}h)'.format(self.Geruestnummer, self.Equipment, self.Stueck, self.Laenge, self.Breite, self.Hoehe, self.Stunde) 
    
    
    
    
#     class Contacts(models.Model):
#         Vorname= models.CharField(max_length = 50, blank = True, verbose_name = 'Vorname')
#         Nachname= models.CharField(max_length = 50, blank = True,  verbose_name = 'Nachname')
#         Email= models.EmailField(max_length =254, blank = True, verbose_name = 'Email')
        
    
    
#         def __str__(self):
#             return '{} {}'.format(self.Vorname, self.Nachname)
