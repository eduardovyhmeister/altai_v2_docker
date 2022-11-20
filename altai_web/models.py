from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from multiselectfield import MultiSelectField # this is installed from the app django-multiselectfield
import numpy as np
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class Users(models.Model):
    first_name = models.CharField('First Name', max_length=120)   #### this is text.
    last_name = models.CharField('Last Name', max_length=120)   #### this is text.
    email_address = models.EmailField('User Email',blank=False)

    def __str__(self): # alows use our model in the admin area    outsi!!!!!!
        return self.first_name + ' ' + self.last_name

class FailureMode(models.Model):
    name = models.TextField(null=True)
    explanation = models.TextField(null=True)
    driver = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    updated = models.DateField(auto_now_add=True)
    driver2 = models.CharField(max_length=100, choices=(
        ('Data','Data'),
        ('Physical','Physical'),
        ('Internal Social','Internal Social'),
        ('User and System Interphase','User and System Interphase'),
        ('Algorithm','Algorithm'),
        ('Other','Other'),),blank=False, null=True)
    failuremodefamily = models.CharField(max_length=100, choices=(
        ('Technical Robustness','Technical Robustness'),
        ('Safety','Safety'),
        ('Transparency','Transparency'),
        ('Accountability','Accountability'),
        ('Societal Wellbeing','Societal Wellbeing'),
        ('Environmental Wellbeing','Environmental Wellbeing'),
        ('Human Agency and Oversight','Human Agency and Oversight'),
        ('Privacy','Privacy'),
        ('Data Governance','Data Governance'),
        ('Diversity,non-discrimination, and fairness','diversity,non-discrimination, and fairness'),
        ('Users Values','Users Values'),
        ('Other','Other'),),blank=False, null=True)

    def save(self,*args,**kwargs): # this allow to automatically save the last modified field
        self.updated = datetime.datetime.today()
        super(FailureMode,self).save(*args,**kwargs)

    def __str__(self):
        return self.name


class Taiprm(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notes = models.TextField()
    porcentage = models.TextField(null=True,default="") # this is the % on how ready is the service
    last_modified = models.DateField(auto_now_add=True)
    publication_date = models.DateField(auto_now_add=True)
    action = models.TextField(null=True,default="")
    status1 = models.BooleanField(default=False)
    status2 = models.BooleanField(default=False)
    status3 = models.BooleanField(default=False)
    status4 = models.BooleanField(default=False)
    status5 = models.BooleanField(default=False)
    status6 = models.BooleanField(default=False)
    status7 = models.BooleanField(default=False)
    status8 = models.BooleanField(default=False)
    status9 = models.BooleanField(default=False)
    # these are exclusive for the risk management process.
    FMEA_OR_CA = models.BooleanField(default=True) # if true FMEA if false CA
    FailureModes = models.ManyToManyField(FailureMode, blank=True,null=True)
    SelectedFailureModes =  models.TextField(null=True,default="[]")
    S = models.TextField(null=True,default="[]")
    O = models.TextField(null=True,default="[]")
    D = models.TextField(null=True,default="[]")
    alpha = models.TextField(null=True,default="[]")
    RPN = models.TextField(null=True,default="[]")
    GRPN = models.TextField(null=True,default="[]")
    AssetRequirements =models.TextField(null=True,default="[]") #a list with the requirements to be branded on the AI asset.
    intrinsic_risk = models.CharField(max_length=255,choices=(('Unacceptable','Unacceptable'),('High','High'),('Limited','Limited'),('Low','Low')),null=True,default='Unacceptable')
    altai = models.TextField(null=True,default="[]")
    ############## these are for the risk register ################################
    IDfailure = models.TextField(null=True,default="[]")
    LinkedID = models.TextField(null=True,default="[]")
    item = models.TextField(null=True,default="[]")
    mode = models.TextField(null=True,default="[]")
    system = models.TextField(null=True,default="[]")
    subsystem = models.TextField(null=True,default="[]")
    description = models.TextField(null=True,default="[]")
    localeffect = models.TextField(null=True,default="[]")
    globaleffect = models.TextField(null=True,default="[]")
    systemstatusatfailing = models.TextField(null=True,default="[]")
    failurecauses = models.TextField(null=True,default="[]")
    itemcausing = models.TextField(null=True,default="[]")
    detectionmethod = models.TextField(null=True,default="[]")
    detectiondescription = models.TextField(null=True,default="[]")
    actionsrecommended = models.TextField(null=True,default="[]")
    actionsresponsible = models.TextField(null=True,default="[]")
    actionstaken = models.TextField(null=True,default="[]")
    KPIprevious = models.TextField(null=True,default="[]")
    ramarksfailuremode = models.TextField(null=True,default="[]")
    #### these are for criticality analysis
    severityclass = models.TextField(null=True,default="[]")
    failureprobabilitysource = models.TextField(null=True,default="[]")
    beta = models.TextField(null=True,default="[]") #failure effect probability
    gama = models.TextField(null=True,default="[]") #failure rate
    operatingtime = models.TextField(null=True,default="[]") # T
    cr = models.TextField(null=True,default="[]")# failure mode criticality number
    ramarkscriticality = models.TextField(null=True,default="[]")
    # general comments
    comments = models.TextField(null=True,default="[]")
    ####################################Risk levels#####################################################
    
    R2_1 = models.IntegerField(null=True,default=200,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    R2_2 = models.IntegerField(null=True,default=800,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    R2_3 = models.IntegerField(null=True,default=1000,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    R3_1 = models.IntegerField(null=True,default=400,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    R3_2 = models.IntegerField(null=True,default=1000,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    R3_3 = models.IntegerField(null=True,default=1000,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    R4_1 = models.IntegerField(null=True,default=800,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    R4_2 = models.IntegerField(null=True,default=1000,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    R4_3 = models.IntegerField(null=True,default=1000,validators=[MaxValueValidator(1000), MinValueValidator(0)])

    
    #### Responses in function of altai and taiprm
    R1 = models.TextField(blank=True,null=True,default="[]")
    R2 = models.TextField(blank=True,null=True,default="[]")
    R3 = models.TextField(blank=True,null=True,default="[]")
    R4 = models.TextField(blank=True,null=True,default="[]")
    R5 = models.TextField(blank=True,null=True,default="[]")
    R6 = models.TextField(blank=True,null=True,default="[]")
    R7 = models.TextField(blank=True,null=True,default="[]")
    ##################################

    User_domain = models.CharField(max_length=100, choices=(
        ('Manufacturing','Manufacturing'),
        ('Aerospace','Aerospace'),
        ('Communications','Communications'),
        ('Chemical and Pharmaceutical','Chemical and pharmaceutical'),
        ('Consumer, Goods and Retail','Consumer, Goods and Retail'),
        ('Energy and Utilities','Energy and Utilities'),
        ('Financial services, Banking and Insurance','Financial services, Banking and Insurance'),
        ('Freight, Logistics and Transportation','Freight, Logistics and Transportation'),
        ('Health and Life Sciences','Health and Life Sciences'),
        ('Hospitality and travel','Hospitality and travel'),
        ('Media, entertainment, and publishing','Media, entertainment, and publishing'),
        ('Technology','Technology'),),blank=False, null=True)
    
    AI_domain =  models.CharField(max_length=100, choices=(
        ('knowldege representation','knowldege representation'),
        ('Automated reasoning','Automated reasoning'),
        ('Common sense reasoning','Common sense reasoning'),
        ('Planning and Scheduling','Planning and Scheduling'),
        ('Searching','Searching'),
        ('Planning - optimisation','Planning - optimisation'),
        ('Machine learning','Machine learning'),
        ('Natural lenguage processing','Natural lenguage processing'),
        ('Computer vision','Computer vision'),
        ('Audio processing','Audio processing'),
        ('Multi-agent systems','Multi-agent systems'),
        ('Robotics and Automation','Robotics and Automation'),
        ('Connected and Automated Vehicles','Connected and Automated Vehicles'),
        ('AI services','AI services'),
        ),blank=False, null=True)

    
    User_Information  = MultiSelectField(choices=(
        ('AI Developer','AI Developer'),
        ('AI Architect','AI Architect'),
        ('Machine Learning Engineer','Machine Learning Engineer'),
        ('Data Analyst','Data Analyst'),
        ('Data Scientist','Data Scientist'),
        ('Academy','Academy'),
        ('AI User','AI User'),
        ('Project Management','Project Management'),
        ('Media','Media'),
        ('Law Enforcement','Law Enforcement'),
        ('Other','Other'),
        ),blank=False, null=True,max_length=1000)
        
    AI_status =  models.CharField(max_length=100,choices=(
        ('Development','Development'),
        ('Deployment','Deployment'),
        ('Use','Use'),
        ('Decomisioning','Decomisioning'),
    ),blank=False, null=True)
    
    options1 =(
        ('Yes','Yes'),
        ('No','No'),
    )

    option9 =(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )

    T1Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified') #is the AI system designed to interact, guide or take decisions by human end-users that affect humans ('subjects ') or society?
    T1Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T1Q2 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified') #Could the AI system generate confusion for some or all end-users or subjects on whether a decision, content, advice or outcome is the result of an algorithmic decision?
    T1Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T1Q3 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified') #Could the AI system generate confusion for some or all end-users or subjects on whether they are interacting with a human or AI system?
    T1Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T1Q4 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') #Are the end-users or subjects informed that they are interacting with an AI? 
    T1Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T1Q5 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Did you put in place any procedure to avoid that the system inadvertently affects human autonomy? 
    T1Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T1Q6 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Could the AI system affect human autonomy by generating over-reliance by end-users?  
    T1Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T1Q7 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Did you put in place procedures to avoid that end-users over-rely on the AI system?  *
    T1Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')

    T2Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q2 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q3 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q4 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q5 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q6 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q7 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q8 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q9 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q10 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q11 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q12 = models.TextField(max_length=500, blank=True, null=True)
    T2Q13 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q14 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q15 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q16 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q17 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q18 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q19 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q20 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q21 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q22 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q23 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q24 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q25 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q26 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q27 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q28 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q29 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q30 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q31 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q32 = models.TextField(max_length=500, blank=True, null=True)
    T2Q33 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q34 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q35 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q36 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q37 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q38 = models.TextField(max_length=500, blank=True, null=True)
    T2Q39 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q40 = models.TextField(max_length=500, blank=True, null=True)
    T2Q41 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q42 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T2Q43 = models.TextField(max_length=500, blank=True, null=True)

    T2Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q9_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q11_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q12_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q13_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q14_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q15_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q16_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q17_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q18_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q19_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q20_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q21_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q22_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q23_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q24_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q25_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q26_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q27_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q28_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q29_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q30_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q31_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q32_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q33_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q34_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q35_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q36_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q37_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q38_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q39_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q40_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q41_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T2Q42_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')



    T3Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q2 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q3 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q4 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q5 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q6 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q7 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q8 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q9 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q10 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q11 = models.TextField(max_length=500, blank=True, null=True)
    T3Q12 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q13 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q14 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q15 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T3Q16 = models.TextField(max_length=500, blank=True, null=True)
    T3Q17 = MultiSelectField(choices=(('Tabular','Tabular'),('Image','Image'),('Text','Text'),('Natural Lenguage','Natural Lenguage'),),blank=False, null=True,max_length=1000)
    T3Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q9_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q12_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q13_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q14_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q15_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T3Q17_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')

    T4Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q2 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q3 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q4 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q5 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q6 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q7 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q8 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q9 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q10 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T4Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q9_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T4Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')

    T5Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T5Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')

    T6Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T6Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T6Q2 = models.TextField(max_length=500, blank=True, null=True)

    T7Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T7Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T7Q2 = models.TextField(max_length=500, blank=True, null=True)

    T8Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T8Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T8Q2 = models.TextField(max_length=500, blank=True, null=True)

    T9Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T9Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T9Q2 = models.TextField(max_length=500, blank=True, null=True)
    T9Q3 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T9Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T9Q4 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T9Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T9Q5 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T9Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')

    T10Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T10Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T10Q2 = models.TextField(max_length=500, blank=True, null=True)

    T11Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T11Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T11Q2 = models.TextField(max_length=500, blank=True, null=True)
    T11Q3 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T11Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T11Q4 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified')
    T11Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    T11Q5 = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # a get_aboslute_url is a function defined to our class than when is used in a POST method it will reverse to the described url.
        return reverse('taiprm_home', args=(str(self.id)))

    def save(self,*args,**kwargs): # this allow to automatically save the last modified field
        ########### this is the code to estimate treat transfer or tolerate.
 
        if self.intrinsic_risk=="High":
            if eval(str(self.GRPN)) <= eval(str(self.R2_1)):
                self.action='Tolerate'
            elif eval(str(self.GRPN)) <= eval(str(self.R2_2)):
                self.action='Treat'
            else:
                self.action='Terminate'
        if self.intrinsic_risk=="Limited":
            if eval(str(self.GRPN)) <= eval(str(self.R3_1)):
                self.action='Tolerate'
            elif eval(str(self.GRPN)) <= eval(str(self.R3_2)):
                self.acition='Treat'
            else:
                self.action='Terminate'
        if self.intrinsic_risk=="Low":
            if eval(str(self.GRPN)) <= eval(str(self.R3_1)):
                self.action='Tolerate'
            elif eval(str(self.GRPN)) <= eval(str(self.R3_2)):
                self.action='Treat'
            else:
                self.action='Terminate'
        ##################
        self.porcentage="width: "+str(int(100*(int(self.status1==True)+int(self.status2==True)+int(self.status3==True)+int(self.status4==True)+int(self.status5==True)+int(self.status6==True)+int(self.status7==True)+int(self.status8==True)+int(self.status9==True))/9))+"%"
        list1=[self.T1Q1,self.T1Q2,self.T1Q3,self.T1Q4,self.T1Q5,self.T1Q6,self.T1Q7]
        list2=[self.T2Q1_2,self.T2Q2_2]
        list3=[self.T3Q1]
        list4=[self.T4Q1]
        list5=[self.T5Q1, self.T4Q1, self.T4Q2, self.T4Q3, self.T4Q4, self.T4Q5, self.T4Q6, self.T4Q7, self.T4Q8, self.T4Q9, self.T4Q10]
        list6=[self.T6Q1, self.T7Q1, self.T8Q1] #root cause analysis
        list7=[self.T9Q1, self.T9Q3, self.T9Q4] # to risk register
        list8=[self.T9Q4] # criticality analysis
        list9=[self.T10Q1] #treatment transfer terminate or tolerate

        if all([elem != 'Unspecified' for elem in list1]):
            self.status1 = True
        else:
            self.status1 = False
        if all([elem != 'Unspecified' for elem in list2]):
            self.status2 = True
        else:
            self.status2 = False
        if all([elem != 'Unspecified' for elem in list3]):
            self.status3 = True
        else:
            self.status3 = False
        if all([elem != 'Unspecified' for elem in list4]):
            self.status4 = True
        else:
            self.status4 = False

        if all([elem != 'Unspecified' for elem in list5]) and any([elem == 'Yes' for elem in list5]):
            self.status5 = True
        else:
            self.status5 = False

        if all([elem != 'Unspecified' for elem in list6]) and all([elem == 'No' for elem in [self.T4Q1, self.T4Q2, self.T4Q3, self.T4Q4, self.T4Q5, self.T4Q6, self.T4Q7, self.T4Q8, self.T4Q9, self.T4Q10]]):
            self.status6 = True
        else:
            self.status6 = False
        if all([elem != 'Unspecified' for elem in list6]):
            self.status7 = True
        else:
            self.status7 = False
        if all([elem != 'Unspecified' for elem in list8]) and self.T9Q4 == 'Yes':
            self.status8 = True
        else:
            self.status8 = True

        if all([elem != 'Unspecified' for elem in list9]) and self.T9Q4 == 'Yes':
            self.status9 = True
        else:
            self.status9 = True
        ####################### depending on feedback set the Trustwortyhy requirements ###############
        if any([elem == 'Yes' for elem in [self.T2Q1,self.T2Q2,self.T2Q3,self.T2Q4,self.T2Q5,self.T2Q6,self.T2Q7,self.T2Q8,self.T2Q9]]):
            self.intrinsic_risk = 'Unacceptable'
        elif any([elem == 'Yes' for elem in [self.T2Q13,self.T2Q14,self.T2Q15,self.T2Q16,self.T2Q17,self.T2Q18,self.T2Q19,self.T2Q20,self.T2Q21,self.T2Q22,self.T2Q23,self.T2Q24,self.T2Q25,self.T2Q26,self.T2Q27,self.T2Q28,self.T2Q29,self.T2Q30]]):
            self.intrinsic_risk = 'High'
            self.AssetRequirements = '["Societal and Environmental Wellbeing","Transparency","Accountability","Human Agency and Oversight","Technical Robustnesss and Safety"]'
        elif any([elem == 'Yes' for elem in [self.T2Q33,self.T2Q34,self.T2Q35,self.T2Q36,self.T2Q37,self.T2Q39]]):
            self.intrinsic_risk = 'Limited'
            self.AssetRequirements = '["Societal and Environmental Wellbeing","Transparency","Technical Robustnesss and Safety"]'
        else:
            self.intrinsic_risk = 'Low'
            self.AssetRequirements = '["Societal and Environmental Wellbeing"]'
        if any([elem == 'Yes' for elem in [self.T3Q1,self.T3Q2,self.T3Q3,self.T3Q4]]):
            self.AssetRequirements = str(eval(self.AssetRequirements)+["Diversity, Non-Discrimination,and Fairness"])
        if any([elem == 'Yes' for elem in [self.T3Q5,self.T3Q6]]):
            self.AssetRequirements = str(eval(self.AssetRequirements)+["Privacy and Data Governance"])
        if any([elem == 'Yes' for elem in [self.T3Q7,self.T3Q8,self.T3Q9,self.T3Q10]]):
            self.AssetRequirements = str(np.unique(eval(self.AssetRequirements)+["Human Agency and Oversight"]))



        R1, R2, R3, R4, R5, R6, R7 = [],[],[],[],[],[],[]
        if self.status9 and ("Human Agency and Oversight" in self.AssetRequirements):
            if self.altai: # ready
                R1 += eval(str(self.R1))
            R1 +=  [' Include a human in the loop, in control, or on the loop for accountability proposes. The decision of the best approach depends on the impact of the decision made (i.e. higher impact higher human involvement) and the system dynamic (e.g. real time control cannot have human-in-the-loop) ']
            R1 += ['Additionally include explainable mechanisms that visualize alternatives and decision paths chosen; to establish users’ responsibilities based on previous considerations.']
            self.R1 = list(dict.fromkeys(R1)) # this clean repetitions

        if self.status9 and ("Technical Robustnesss and Safety" in self.AssetRequirements):
            if self.altai: # ready
                R2 += eval(str(self.R2))

            R2 +=  ['The Robustness should points to the user to understand yhe needs of the system with respect to recovery of failures and, at the same time, improve its performance. Thefore, please consider specify the system performance metrics, perform functional testing, check performance through benchmarking, test the development using simulation, setup an environment for anomaly monitoring, set fail-safe mechanisms, set hardware security, and define data quality/quantity improvements.']
            R2 += ['Consider specify the system performance metrics']
            R2 += ['Consider to perform functional testing']
            R2 += ['Consider to perform performance checking through benchmarking']
            R2 += ['test the development using simulation']
            R2 += ['Consideer to setup an environment for anomaly monitoring']
            R2 += ['Consider to set set fail-safe mechanisms']
            R2 += ['Consider to set set hardware security']
            R2 += ['Define approaches to data quality/quantity improvements.']
            R2 += ['Consider the implementation of Blochain to improve safety and system security']
            R2 += ['Consider the implementation of Federated learning to improve safety and system security']

            self.R2 = list(dict.fromkeys(R2)) # this clean repetitions
        
        if self.status9 and ("Privacy and Data Governance" in self.AssetRequirements):
            if self.altai: # ready
                R3 += eval(str(self.R3))
            R3 +=  ['Try to avoid to collect or store GDPR sensitive data']
            R3 += ['Place strict deadlines to minimise personal data retention']
            R3 += ['Set protocols on IT security analysis']
            R3 += ['Make sure to train operators for data/sensitive data processing']
            R3 += ['Assess the possibility of using anonymised or pseudonymised data']
            R3 += [' Secure to inform users on the management (and how) its information will be used in case cannot be considered avoidance of use of personal information and its anonymisation']
            R3 += ['Provide a contact point for individuals to raise concerns related to Privacy and Data governance in case cannot be considered avoidance of use of personal information and its anonymisation']
            R3 += ['Consider the implementation of Blochain to improve safety and system security']
            R3 += ['Consider the implementation of Federated learning to improve safety and system security']
            self.R3 = list(dict.fromkeys(R3)) # this clean repetitions

        if self.status9 and ("Transparency" in self.AssetRequirements):
            if self.altai: # ready
                R4 += eval(str(self.R4))
            if self.T3Q17 == 'Tabular':
                R4 += ['Consider the use of Feature importance, Rule-Based, Prototypes, and Counterfactual approaches for improve explainability']
            if self.T3Q17 == 'Image':
                R4 += ['Consider  approaches such as Saliency Maps, Concepts Attribute, Counterfactual, and Prototypes for improve explainability']
            if self.T3Q17  == 'Text' or self.T3Q17 == 'Natural Lenguage':
                R4 += ['Consider approaches such as Sentence Highlight and Attention-Based Method for improve explainability']
            R4 += ['Define metrics to evaluate explainaiblity capabilities of your design ']
            R4 +=  ['To secure traceability define adequate documentation and protocols to keep records of data provenance, requirement, architecture, codes, minutes, and different text used to specify AI functionalities and updates']
            R4 += ['Define protocols that enable the reporting of failure conditions of each incident in which the AI artifact is present (ntails to establish actions to monitor anomalies on data and processe)']
            R4 += ['Consider the implementation of Blochain to improve safety and system security']
            R4 += ['Consider the implementation of MLOPs and other management protocols to improve transparency']
            self.R4 = list(dict.fromkeys(R4)) # this clean repetitions

        if self.status9 and ("Diversity, Non-Discrimination,and Fairness" in self.AssetRequirements):
            if self.altai: # ready
                R5 += eval(str(self.R5))
            R5 +=  ['']
            self.R5 = list(dict.fromkeys(R5)) # this clean repetitions

        if self.status9 and ("Societal and Environmental Wellbeing" in self.AssetRequirements):
            if self.altai: # ready
                R6 += eval(str(self.R6))
            R6 += ['Considering the modification and update of processes timeframes of metaparameters of the AI artifact to reduce the energy use during the configuration of parameters and deployment processes while securing system robustness']
            R6 += ['It should be consider to secure the saving of runs results in highly energy-intensive processes such as optimization and to provide a method to reuse the result']
            R6 += ['Run dimensionality process to secure iterative tasks processes on variables that are statistically the same, and to suppress recording unnecessary data']
            R7 += ['Incorporate methods and adequate testing techniques to secure the reduction of the computational burden ']
            self.R6 = list(dict.fromkeys(R6)) # this clean repetitions

        if self.status9 and ("Accountability" in self.AssetRequirements):
            if self.altai: # ready
                R7 += eval(str(self.R7))
            R7 +=  ['Establish Responsibilities on AI failing Conditions and secure to document them properly (hte developers should be accountable for faults due to product’s design while users must be accountable for faults resulting from the design requirements and the operation of the AI artifact.)']
            R7 += ['Consider the implementation of MLOPs or well documented apporaches to trach the development process']
            self.R7 = list(dict.fromkeys(R7)) # this clean repetitions

        self.last_modified = datetime.datetime.today()
        super(Taiprm,self).save(*args,**kwargs)


class Assessment(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    taiprm = models.ForeignKey(Taiprm, blank=True, null=True, on_delete=models.CASCADE)
    notes = models.TextField(blank=True,null=True)
    porcentage = models.TextField(null=True,default="0")
    R1 = models.TextField(blank=True,null=True)
    R2 = models.TextField(blank=True,null=True)
    R3 = models.TextField(blank=True,null=True)
    R4 = models.TextField(blank=True,null=True)
    R5 = models.TextField(blank=True,null=True)
    R6 = models.TextField(blank=True,null=True)
    R7 = models.TextField(blank=True,null=True)
    last_modified = models.DateField(auto_now_add=True)
    publication_date = models.DateField(auto_now_add=True)
    status1 = models.BooleanField(default=False)
    status2 = models.BooleanField(default=False)
    status3 = models.BooleanField(default=False)
    status4 = models.BooleanField(default=False)
    status5 = models.BooleanField(default=False)
    status6 = models.BooleanField(default=False)
    status7 = models.BooleanField(default=False)
    recommendations1=models.CharField(max_length=10000,blank=True,null=True,default='[]')
    recommendations2=models.CharField(max_length=10000,blank=True,null=True,default='[]')
    recommendations3=models.CharField(max_length=10000,blank=True,null=True,default='[]')
    recommendations4=models.CharField(max_length=10000,blank=True,null=True,default='[]')
    recommendations5=models.CharField(max_length=10000,blank=True,null=True,default='[]')
    recommendations6=models.CharField(max_length=10000,blank=True,null=True,default='[]')
    recommendations7=models.CharField(max_length=10000,blank=True,null=True,default='[]')
    User_domain = models.CharField(max_length=100, choices=(
        ('Manufacturing','Manufacturing'),
        ('Aerospace','Aerospace'),
        ('Communications','Communications'),
        ('Chemical and Pharmaceutical','Chemical and pharmaceutical'),
        ('Consumer, Goods and Retail','Consumer, Goods and Retail'),
        ('Energy and Utilities','Energy and Utilities'),
        ('Financial services, Banking and Insurance','Financial services, Banking and Insurance'),
        ('Freight, Logistics and Transportation','Freight, Logistics and Transportation'),
        ('Health and Life Sciences','Health and Life Sciences'),
        ('Hospitality and travel','Hospitality and travel'),
        ('Media, entertainment, and publishing','Media, entertainment, and publishing'),
        ('Technology','Technology'),),blank=False, null=True)
    AI_domain =  models.CharField(max_length=100, choices=(
        ('knowldege representation','knowldege representation'),
        ('Automated reasoning','Automated reasoning'),
        ('Common sense reasoning','Common sense reasoning'),
        ('Planning and Scheduling','Planning and Scheduling'),
        ('Searching','Searching'),
        ('Planning - optimisation','Planning - optimisation'),
        ('Machine learning','Machine learning'),
        ('Natural lenguage processing','Natural lenguage processing'),
        ('Computer vision','Computer vision'),
        ('Audio processing','Audio processing'),
        ('Multi-agent systems','Multi-agent systems'),
        ('Robotics and Automation','Robotics and Automation'),
        ('Connected and Automated Vehicles','Connected and Automated Vehicles'),
        ('AI services','AI services'),
        ),blank=False, null=True)
    AI_stakeholder_type =  models.CharField(max_length=100, choices=(
        ('Academic ','Academic'),
        ('Innovator / SME ','Innovator / SME '),
        ('Policy maker','Policy maker'),
        ('Larch industry','Larch industry'),
        ('RTO','RTO'),
        ('Public administration','Public administration'),
        ),blank=False, null=True)
    User_Information  = MultiSelectField(choices=(
        ('AI Developer','AI Developer'),
        ('AI Architect','AI Architect'),
        ('Machine Learning Engineer','Machine Learning Engineer'),
        ('Data Analyst', 'Data Analyst'),
        ('Data Scientist', 'Data Scientist'),
        ('Academy','Academy'),
        ('AI User','AI User'),
        ('Project Management','Project Management'),
        ('Media','Media'),
        ('Law Enforcement','Law Enforcement'),
        ('Other','Other'),
        ),blank=False, null=True, max_length=1000)
    AI_status =  models.CharField(max_length=100,choices=(
        ('Development','Development'),
        ('Deployment','Deployment'),
        ('Use','Use'),
        ('Decomisioning','Decomisioning'),
    ),blank=False, null=True)
    options1 =(('Yes','Yes'),('To Some extent','To Some extent'),('No','No'),("Don't know","Don't know"),)
    options2 =(('Yes','Yes'),('No','No'),)
    options3 =(('5','Non-existent'),('4','Low'),('3','Moderate'),('2','Significant'),('1','High'),)
    options4 =(('Yes','Yes'),('No','No'),("Don't know","Don't know"),)
    options5 =(('1','Non-existent'),('2','Completely inadequate'),('3','Almost adequate'),('4','Adequate'),('5','Fully adequate'),)
    options6 =(('Yes','Yes'),('No','No'),('Not applicable','Not applicable'),)
    options8 =(('Impossibl','Impossible'),('Unlikely','Unlikely'),('Possible','Possible'),('Likely','Likely'),)
    option9 =(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),)

    A1Q1 = models.CharField(max_length=100, choices=options1,blank=False, null=True, default='Unspecified') #is the AI system designed to interact, guide or take decisions by human end-users that affect humans ('subjects ') or society?
    A1Q2 = models.CharField(max_length=100, choices=options2,blank=False, null=True, default='Unspecified') #Could the AI system generate confusion for some or all end-users or subjects on whether a decision, content, advice or outcome is the result of an algorithmic decision?
    A1Q3 = models.CharField(max_length=100, choices=options2,blank=False, null=True, default='Unspecified') #Could the AI system generate confusion for some or all end-users or subjects on whether they are interacting with a human or AI system?
    A1Q4 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') #Are the end-users or subjects informed that they are interacting with an AI? 
    A1Q5 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you put in place any procedure to avoid that the system inadvertently affects human autonomy? 
    A1Q6 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Could the AI system affect human autonomy by generating over-reliance by end-users?  
    A1Q7 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you put in place procedures to avoid that end-users over-rely on the AI system?  *
    A1Q8 = models.TextField(max_length=500, blank=True, null=True) #please explain
    A1Q9 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Could the AI system affect human autonomy by interfering with the (end-user’s decision-making process in any other (unintended) way?
    A1Q10 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you put in place any procedure to avoid that the system inadvertently affects human autonomy? 
    A1Q11 = models.TextField(max_length=500, blank=True, null=True) #please explain
    A1Q12 = models.CharField(max_length=100,choices=options3, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the risk that the AI system negatively affects human autonomy? 
    A1Q13 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # How would you rate the measures you have adopted to mitigate this risk? * 
    A1Q14 = models.CharField(max_length=100,choices=options8, blank=False, null=True, default='Unspecified') # Does the AI system create one of the following risks?
    A1Q15 = models.CharField(max_length=100,choices=options8, blank=False, null=True, default='Unspecified') # Does the AI system create one of the following risks?
    A1Q16 = models.CharField(max_length=100,choices=options8, blank=False, null=True, default='Unspecified') # Does the AI system create one of the following risks?
    A1Q17 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you take measures to deal with possible negative consequences for end-users or subjects in case they develop a disproportionate attachment to?
    A1Q18 = models.TextField(max_length=500, blank=True, null=True) #Please describe whether the AI system (tick as many as appropriate)
    A1Q19 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you take measures to minimise the risk of addiction?
    A1Q20 = models.TextField(max_length=100, blank=True, null=True) #Please describe whether the AI system (tick as many as appropriate)
    A1Q21 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you take measures to mitigate the risk of manipulation?
    A1Q22 = models.TextField(max_length=100, blank=True, null=True) #Please describe the measures:
    A1Q23 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # How would you rate the measures you have adopted to mitigate this risk?
    A1Q24 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Please describe whether the AI system (tick as many as appropriate)
    A1Q25 = MultiSelectField(choices=((1,'Is a self-learning or autnomous system'),(2,'Is overseen by a human-in-the-loop'),(3,'Is overseen by a human-in-the-loop'),(4,'Is overseen by a human-in-command'),(5, 'other'),(6, 'Do not know'),),max_length=1000)
    A1Q26 = models.TextField(max_length=100, blank=True, null=True) #Please describe the measures:
    A1Q27 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you put in place any procedure to avoid that the system inadvertently affects human autonomy? 
    A1Q28 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you put in place any procedure to avoid that the system inadvertently affects human autonomy? 
    A1Q29 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you put in place any procedure to avoid that the system inadvertently affects human autonomy? 
    A1Q30 = models.CharField(max_length=100, choices=(("Abort the process entirely","Abort the process entirely"),("Abort the process in part","Abort the process in part"),("Delegate control to a human","Delegate control to a human"),("Other","Other"),("Don't know","Don't know")), blank=False, null=True, default='Unspecified') # Did you put in place any procedure to avoid that the system inadvertently affects human autonomy? 
    A1Q31 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you put in place any procedure to avoid that the system inadvertently affects human autonomy? 
    A1Q32 = models.CharField(max_length=100, choices=options5, blank=False, null=True, default='Unspecified')

    A1Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q9_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q12_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q13_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q14_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q17_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q19_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q21_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q23_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q24_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q25_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q27_2 = models.CharField(max_length=100, choices=option9, blank=False, null=True, default='Unspecified')
    A1Q28_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q29_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q30_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q31_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A1Q32_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')


    # Robustness
    A2Q1 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Is the AI system certified for cybersecurity (e.g., the certification scheme created by the Cybersecurity Act in Europe) or is it compliant with specific security standards?
    A2Q2 = models.CharField(max_length=100, blank=False, null=True, default='Unspecified', choices=(('Exposed','Exposed'),('To some extent','To some extent'),('Not exposed','Not exposed'),('Do not know', 'Do not know'),))
    A2Q3 = models.CharField(max_length=100, blank=False, null=True, choices=options2, default='Unspecified') # Did you assess potential forms of attacks to which the AI system could be vulnerable?
    A2Q4 = models.CharField(max_length=100, blank=False, null=True, default='Unspecified', choices=(('Data poisoning','Data poisoning (i.e. manipulation of the training data)'),('Model evasion','Model evasion (i.e., classify the data according to the attacker will)'),('Model inversion','Model inversion (i.e. infer the model parameters)'),('Other','Other'),)) # Did you consider different types of vulnerabilities and potential entry points for attacks such as:
    A2Q5 = models.CharField(max_length=100, blank=False, null=True, choices=options2, default='Unspecified') # Did you put measures in place to ensure the integrity, robustness and overall security of the AI system against potential attacks over its lifecycle?
    A2Q6 = models.TextField(max_length=500, blank=True, null=True) #please explain
    A2Q7 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') #Did you red-team/pen test the system?
    A2Q8 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified')  #Do you inform end-users of the duration of security coverage and updates?
    A2Q9 = models.TextField(max_length=500, blank=True, null=True) #How long is the expected timeframe within which you will provide security updates for your system?
    A2Q10 = models.CharField(max_length=100,choices=options3, blank=False, null=True, default='Unspecified') #Based on your answers to the previous questions, how would you rate the resilience to attacks of the AI system?
    A2Q11 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the measures you have adopted to ensure resilience? 
    A2Q12 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Could the AI system have adversarial, critical or damaging effects (e.g., to human or societal safety) in case of risks or threats such as design or technical faults, defects, outages, attacks, misuse, inappropriate or malicious use?  *
    A2Q13 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you define risk, risk metrics and risk levels of the AI system in each specific use case? *
    A2Q14 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Could a low level of accuracy of the AI system have critical, adversarial or damaging consequences?
    A2Q15 = models.TextField(max_length=500, blank=True, null=True) #please explain
    A2Q16 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you put in place measures to ensure that the data (including training data) used to develop the AI system is up to date, of high quality, complete and representative of the environment the system will be deployed in? 
    A2Q17 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you put in place a series of steps to monitor, and document the AI system’s accuracy? 
    A2Q18 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you consider whether the AI system's operation can invalidate the data or assumptions it was trained on, and how this might lead to adversarial effects (e.g. biased estimators, echo chambers etc.)?
    A2Q19 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you put processes in place to ensure that the level of accuracy of the AI system to be expected by end-users and/or subjects is properly communicated?
    A2Q20 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the risk that the AI system's accuracy drops below intended level? 
    A2Q21 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # How would you rate the measures you have adopted to ensure system accuracy?
    A2Q22 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Could the AI system cause critical, adversarial or damaging consequences (e.g., pertaining to human safety) in case of low reliability and/or reproduciblity?
    A2Q23 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you test whether specific contexts or conditions need to be taken into account to ensure reproducibility? 
    A2Q24 = models.CharField(max_length=100, choices=options3, blank=False, null=True, default='Unspecified') # Did you put in place verification and validation methods and documentation (e.g. logging) to evaluate and ensure different aspects of the system’s reliability and reproducibility? 
    A2Q25 = models.CharField(max_length=100, choices=options5, blank=False, null=True, default='Unspecified') # Did you clearly document and operationalize processes for the testing and verification of the reliability and reproducibility of the AI system? *
    A2Q26 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you define tested failsafe fallback plans to address AI system errors of whatever origin and put governance procedures in place to trigger them? *
    A2Q27 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you put in place a proper procedure for handling the cases where the AI system yields results with a low confidence score? *
    A2Q28 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Is your AI system using online continual learning? *
    A2Q29 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you consider potential negative consequences from the AI system learning novel or unusual methods to score well on its objective function?
    A2Q30 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the reliability of the AI system? *
    A2Q31 = models.CharField(max_length=100,choices=options3, blank=False, null=True, default='Unspecified') # How would you rate the measures you have adopted to ensure system reliability? 
    A2Q32 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the reproducibility of the AI system? 
    A2Q33 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # How would you rate the measures you have adopted to ensure system reproducibility? *
    A2Q34 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q35 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q36 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q37 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q38 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q39 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q40 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q41 = models.CharField(max_length=100,choices=options4, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q42 = models.CharField(max_length=100,choices=options3, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q43 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q44 = models.CharField(max_length=100,choices=options3, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q45 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 
    A2Q46 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the fall-back you have adopted? 

    A2Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q11_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q12_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q13_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q14_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q16_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q17_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q18_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q19_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q20_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q21_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q22_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q23_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q24_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q25_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q26_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q27_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q28_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q29_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q30_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q31_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q32_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q33_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q34_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q35_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q36_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q37_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q38_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q39_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q40_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q41_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q42_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q43_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q44_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A2Q45_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A2Q46_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')

    #privacy and data governance
    A3Q1 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you consider the impact of the AI system on the right to privacy, the right to physical, mental and/or moral integrity and the right to data protection? 
    A3Q2 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Depending on the use case, did you establish mechanisms that allow flagging issues related to privacy or data protection concerning the AI system?
    A3Q3 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Is your AI system being trained, or was it developed, by using or processing personal data (including special categories of personal data)? 
    A3Q4 = MultiSelectField(choices=((1,'Data Protection Impact Assessment'),(2,'Designate a Data Protection Officer (DPO) and include him/her at an early stage in the development, procurement or use phase of the AI system'),(3,'Oversight mechanisms for data processing (incl. limited access by qualified organisation members, mechanisms for logging data access and modifications)'),(4,' Measures to enhance privacy by design and default (e.g., =gb=encryption, pseudonymisation, aggregation, anonymisation=ge=) '),(5,'Data minimisation, in particular personal data (incl. special categories of data)'),),max_length=1000)
    A3Q5 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you implement the right to withdraw consent, the right to object and the right to be forgotten in the AI system?
    A3Q6 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you consider the privacy and data protection implications of data collected, generated or processed over the course of the AI system's
    A3Q7 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you consider the privacy and data protection implications of the AI system's non-personal training-data or other processed non-personal data?
    A3Q8 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you align the AI system with relevant standards (e.g. ISO, IEEE) or widely adopted protocols for (daily) data management and governance? *
    A3Q9 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the privacy & data governance measures and procedures you have set up for the AI system? *

    A3Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A3Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A3Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A3Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A3Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A3Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A3Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A3Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A3Q9_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 

    # transparency
    A4Q1 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Did you put in place measures to continuously assess the quality of the input data to the AI system? *
    A4Q2 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified')
    A4Q3 = models.TextField(max_length=500, blank=True, null=True)
    A4Q4 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified')
    A4Q5 = models.TextField(max_length=500, blank=True, null=True)
    A4Q6 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified')
    A4Q7 = models.TextField(max_length=500, blank=True, null=True)
    A4Q8 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Did you explain the decision of the AI system to the users? *
    A4Q9 = models.TextField(max_length=500, blank=True, null=True) # please explain
    A4Q10 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Do you continuously survey the users to ask them whether they understand the decision(s) of the AI system? *
    A4Q11 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # In cases of interactive AI systems (e.g., chatbots, robo-lawyers), do you communicate to users that they are interacting with an AI system instead of a human? *
    A4Q12 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you establish mechanisms to inform users about the purpose, criteria and limitations of the decision(s) generated by the AI system? *
    A4Q13 = models.TextField(max_length=500, blank=True, null=True)
    A4Q14 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Did you communicate the technical limitations and potential risks of the AI system to end-users, such as its level of accuracy and/or error rates? *
    A4Q15 = models.TextField(max_length=500, blank=True, null=True) # plase explain
    A4Q16 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you provide appropriate training material and disclaimers to users on how to adequately use the AI system? *
    A4Q17 = models.TextField(max_length=500, blank=True, null=True) # please explain
    A4Q18 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the measures you have adopted to ensure transparency?

    A4Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A4Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A4Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A4Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A4Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A4Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A4Q11_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A4Q12_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A4Q14_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A4Q16_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A4Q18_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 

    # Diversity, non -discrimination and fairness
    A5Q1 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you establish a strategy or a set of procedures to avoid creating or reinforcing unfair bias in the AI system, both regarding the use of input data as well as for the algorithm design?
    A5Q2 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you consider diversity and representativeness of end-users and/or subjects in the data?
    A5Q3 = models.CharField(max_length=100, choices=options6, blank=False, null=True, default='Unspecified') # Did you test for specific target groups or problematic use case?
    A5Q4 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you research and use publicly available technical tools, that are state-of-the-art, to improve your understanding of the data, model and performance?
    A5Q5 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Did you assess and put in place processes to test and monitor for potential biases during the entire lifecycle of the AI system (e.g. biases due to possible limitations stemming from the composition of the used data sets (lack of diversity, non-representativeness))?
    A5Q6 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Where relevant, did you consider diversity and representativeness of end-users and or subjects in the data?
    A5Q7 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Did you put in place educational and awareness initiatives to help AI designers and AI developers be more aware of the possible bias they can inject in designing and developing the AI system?
    A5Q8 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Depending on the use case, did you ensure a mechanism that allows for the flagging of issues related to bias, discrimination or poor performance of the AI system?
    A5Q9 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you establish clear steps and ways of communicating on how and to whom such issues can be raised?
    A5Q10 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you identify the subjects that could potentially be (in)directly affected by the AI system, in addition to the end-users?
    A5Q11 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Is your definition of fairness commonly used and implemented in any phase of the process of setting up the AI system ?
    A5Q12 = models.TextField(max_length=500, blank=True, null=True) # Please explain your definition of fairness:
    A5Q13 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you consider other definitions of fairness before choosing this one?
    A5Q14 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you consult with the impacted communities about the correct definition of fairness, i.e., representatives of elderly persons or persons with disabilities?
    A5Q15 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you ensure a quantitative analysis or metrics to measure and test the applied definition of fairness?
    A5Q16 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you establish mechanisms to ensure fairness in your AI system?
    A5Q17 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the measures you have adopted to detect and avoid bias, and ensure fairness?
    A5Q18 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q19 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q20 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q21 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q22 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q23 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q24 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q25 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q26 = models.TextField(max_length=500, blank=True, null=True) 
    A5Q27 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q28 = models.TextField(max_length=500, blank=True, null=True) 
    A5Q29 = models.CharField(max_length=500, choices=options5, blank=False, null=True, default='Unspecified')
    A5Q30 = models.CharField(max_length=500, choices=options2, blank=False, null=True, default='Unspecified')
    A5Q31 = models.CharField(max_length=500, choices=options5, blank=False, null=True, default='Unspecified')

    A5Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q9_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q11_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q13_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q14_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q15_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q16_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q17_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q18_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q19_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q20_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q21_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q22_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q23_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q24_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q25_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q27_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q29_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q30_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A5Q31_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 

    # societal and environmental well-being
    A6Q1 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Are there potential negative impacts of the AI system on the environment?
    A6Q2 = models.TextField(max_length=500, blank=True, null=True) 
    A6Q3 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Where possible, did you establish mechanisms to evaluate the environmental impact of the AI system’s development, deployment and/or use (for example amount of energy used and carbon emissions)?
    A6Q4 = models.TextField(max_length=500, blank=True, null=True) 
    A6Q5 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you define measures to reduce the environmental impact of the AI system throughout its lifecycle? *
    A6Q6 = models.TextField(max_length=500, blank=True, null=True) 
    A6Q7 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the risk that the AI system negatively affects the environment? *
    A6Q8 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # How would you rate the measures you have adopted to mitigate this risk? *
    A6Q9 = models.CharField(max_length=100, choices=options1, blank=False, null=True, default='Unspecified') # Does the AI system impact human work and work arrangements?  *
    A6Q10 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you pave the way for the introduction of the AI system in your organisation by informing and consulting with impacted workers and their representatives (trade unions, (European) work councils) in advance?  *
    A6Q11 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you adopt measures to ensure that the work impacts of the AI system are well understood?  *
    A6Q12 = models.TextField(max_length=500, blank=True, null=True) 
    A6Q13 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Could the AI system create the risk of de-skilling of the workforce? *
    A6Q14 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified')
    A6Q15 = models.TextField(max_length=500, blank=True, null=True) 
    A6Q16 = models.CharField(max_length=100, choices=options2, blank=False, null=True, default='Unspecified') # Did you provide training opportunities and materials for re- and up-skilling measures? *
    A6Q17 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on your answers to the previous questions, how would you rate the risk that the AI system negatively impacts work and work arrangements? *
    A6Q18 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # How would you rate the measures you have adopted to mitigate this risk? *
    A6Q19 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified')
    A6Q20 = models.TextField(max_length=500, blank=True, null=True) 

    A6Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q9_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q11_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q13_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q14_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q16_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q17_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified') 
    A6Q18_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A6Q19_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')

 # Accountability
    A7Q1 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you establish mechanisms that facilitate the AI system’s auditability (e.g. traceability of the development process, the sourcing of training data and the logging of the AI system’s processes, outcomes, positive and negative impact)?  *
    A7Q2 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you ensure that the AI system can be audited by independent third parties?  *
    A7Q3 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') #Based on the answer you gave above, do you believe the measures in place to ensure the auditability of the AI system are: *
    A7Q4 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you foresee any kind of external guidance or third-party auditing processes to oversee ethical concerns and accountability measures?  *
    A7Q5 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Does the involvement of these third parties go beyond the development phase?  *
    A7Q6 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you organise risk training and, if so, does this also inform about the potential legal framework applicable to the AI system?  *
    A7Q7 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you consider establishing an ‘AI ethics review board’ or a similar mechanism to discuss the overall accountability and ethics practices, including potential unclear grey areas?  *
    A7Q8 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you establish a mechanism to identify conflicts of values that could be implemented in your AI system and your own interests? *
    A7Q9 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Does this process include identification and documentation of trade-offs between different ethical principles?  *
    A7Q10 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # How did you decide on such trade-offs? Did you ensure that the trade-off decision was documented? *
    A7Q11 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Did you establish a processes for third parties (e.g. suppliers, end-users, subjects, distributors/vendors or workers) or workers to report potential vulnerabilities, risks or biases in the AI system? *
    A7Q12 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified') # Does this process foster revision of the risk management process? *
    A7Q13 = models.CharField(max_length=100, choices=options4, blank=False, null=True, default='Unspecified')  # For applications that can significantly adversely affect individuals, have redress by design mechanisms been put in place? *
    A7Q14 = models.CharField(max_length=100,choices=options5, blank=False, null=True, default='Unspecified') # Based on the answer you gave above, do you believe the risk management system you have in place is: *

    A7Q1_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q2_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q3_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q4_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q5_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q6_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q7_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q8_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q9_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q10_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q11_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q12_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q13_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')
    A7Q14_2 = models.CharField(max_length=100, choices=option9,blank=False, null=True, default='Unspecified')

    def __str__(self):
        return self.title

    def get_absolute_url(self): # a get_aboslute_url is a function defined to our class than when is used in a POST method it will reverse to the described url.
        return reverse('assess_home', args=(str(self.id)))

    def save(self): # this allow to automatically save the last modified field
        self.porcentage="width: "+str(int(100*(int(self.status1==True)+int(self.status2==True)+int(self.status3==True)+int(self.status4==True)+int(self.status5==True)+int(self.status6==True)+int(self.status7==True))/7))+"%"
        options = ["No","Don't know", "To some extent"]
        R1, R2, R3, R4, R5, R6, R7 = [],[],[],[],[],[],[]
        list1=[self.A1Q1,self.A1Q2,self.A1Q3,self.A1Q4,self.A1Q5,self.A1Q6,self.A1Q7,self.A1Q8,self.A1Q9,self.A1Q10,self.A1Q11,self.A1Q12,self.A1Q13,self.A1Q14,self.A1Q15,self.A1Q16,self.A1Q17,self.A1Q18,self.A1Q19,self.A1Q20,self.A1Q21,self.A1Q22,self.A1Q23,self.A1Q24,self.A1Q25,self.A1Q26,self.A1Q27,self.A1Q28]
        list2=[self.A2Q1,self.A2Q2,self.A2Q3,self.A2Q4,self.A2Q5,self.A2Q6,self.A2Q7,self.A2Q8,self.A2Q9,self.A2Q10,self.A2Q11,self.A2Q12,self.A2Q13,self.A2Q14,self.A2Q15,self.A2Q16,self.A2Q17,self.A2Q18,self.A2Q19,self.A2Q20,self.A2Q21,self.A2Q22,self.A2Q23,self.A2Q24,self.A2Q25,self.A2Q26,self.A2Q27,self.A2Q28,self.A2Q29,self.A2Q30,self.A2Q31,self.A2Q32,self.A2Q33,self.A2Q34,self.A2Q35,self.A2Q36,self.A2Q37,self.A2Q38,self.A2Q39,self.A2Q40,self.A2Q41,self.A2Q42,self.A2Q43,self.A2Q44,self.A2Q45]
        list3=[self.A3Q1,self.A3Q2,self.A3Q3,self.A3Q4,self.A3Q5,self.A3Q6,self.A3Q7,self.A3Q8,self.A3Q9]
        list4=[self.A4Q1,self.A4Q2,self.A4Q3,self.A4Q4,self.A4Q5,self.A4Q6,self.A4Q7,self.A4Q8,self.A4Q9,self.A4Q10,self.A4Q11,self.A4Q12]
        list5=[self.A5Q1,self.A5Q2,self.A5Q3,self.A5Q4,self.A5Q5,self.A5Q6,self.A5Q7,self.A5Q8,self.A5Q9,self.A5Q10,self.A5Q11,self.A5Q12,self.A5Q13,self.A5Q14,self.A5Q15,self.A5Q16,self.A5Q17,self.A5Q18,self.A5Q19,self.A5Q20,self.A5Q21,self.A5Q22,self.A5Q23,self.A5Q24,self.A5Q25,self.A5Q26,self.A5Q27,self.A5Q28,self.A5Q29,self.A5Q30,self.A5Q31]
        list6=[self.A6Q1,self.A6Q2,self.A6Q3,self.A6Q4,self.A6Q5,self.A6Q6,self.A6Q7,self.A6Q8,self.A6Q9,self.A6Q10,self.A6Q11,self.A6Q12,self.A6Q13,self.A6Q14,self.A6Q15,self.A6Q16,self.A6Q17,self.A6Q18]
        list7=[self.A7Q1,self.A7Q2,self.A7Q3,self.A7Q4,self.A7Q5,self.A7Q6,self.A7Q7,self.A7Q8,self.A7Q9,self.A7Q10,self.A7Q11,self.A7Q12,self.A7Q13,self.A7Q14]
        if all([elem != 'Unspecified' for elem in list1]):
            self.status1 = True
            if self.A1Q3 in options: # ready
                R1 += ["Incorporate a process where end-users and/or subjects are adequately made aware that an AI-system influenced the decision, content, advice or outcome."]
            if self.A1Q5 in options: # ready
                R1+=["Ensure that the end-users or subjects are adequately informed that they are interacting with an AI system."]
            if self.A1Q7 in options: # ready
                R1+=["Put in place procedures to avoid that end users over-rely on the AI system."]
            if self.A1Q10 in options: # ready
                R1+=["Put in place any procedure to avoid that the system inadvertently affects human autonomy. "]
            if self.A1Q17 in options: # ready
                R1+=["Take measures to deal with the possible negative consequences for end-users or subjects in case they develop attachment. In particular, provide means for the user to have control of the interactions."]
            if self.A1Q19 in options: # ready
                R1+=["Take measures to minimize the risk of addiction by involving experts from other disciplines such as psychology and social work."]
            if self.A1Q21 in options: # ready
                R1+=["Take measures to mitigate the risk of manipulation, including providing clear information about ownership and aims of the system, avoiding unjustified surveillance, and preserving autonomy and mental health of users."]
            if self.A1Q27 in options: # ready
                R1+=["Give specific training to humans (human-in-the-loop, human-on-the-loop, human-in-command) on how to exercise oversight."]
            if self.A1Q28 in options: # ready
                R1+=["Establish detection and response mechanisms in case the AI system generates undesirable adverse effects for the end-user or subject."]
            if self.A1Q29 in options: # ready
                R1+=["Deploy a “stop button” or procedure to safely abort an operation when needed."]
            if self.A1Q31 in options: # ready
                R1+=["Adopt specific oversight and control measures to reflect the self-learning/autonomous nature of the system."]
            self.R1=R1
        else:
            self.status1 = False
            self.R1=[]

        if all([elem != 'Unspecified' for elem in list2]):
            self.status2 = True
            if self.A2Q3 in options: # ready
                R2+=["Assess potential forms of attacks to which the AI system could be vulnerable."]
            if self.A2Q5 in options: # ready
                R2+=["Put in place measures to ensure the integrity, robustness and overall security of the AI system against potential attacks over its lifecycle."]
            if self.A2Q7 in options: #ready
                R2+=["Red-team/pentest the system"]
            if self.A2Q8 in options : #ready
                R2+=["Inform users as soon as possible if some new threats are detected."]
            if self.A2Q13 in options: #ready
                R2+=["Define risk, risk metrics and risk levels of the AI system in each specific use case."]
            if self.A2Q14 in options: #ready
                R2+=["Put in place a process to continuously measure and assess risks."]
            if self.A2Q16 in options: # ready
                R2+=["Inform end-users and subjects of existing or potential risks."]
            if self.A2Q17 in options: #ready
                R2+=["Identify the possible threats to the AI system (design faults, technical faults, environmental threats) and the possible resulting consequences."]
            if self.A2Q18 in options:
                R2+=["Assess the risk of possible malicious use, misuse or inappropriate use of the AI system."] # ready
            if self.A2Q19 in options:
                R2+=["Assess the dependency of critical system's decisions on its stable and reliable behaviour."] # ready
            if self.A2Q20 in options: #ready
                R2+=["Assess the dependency of critical system's decisions on its stable and reliable behaviour."]
            if self.A2Q21 in options: #ready
                R2+=["Align the reliability/testing requirements to the appropriate levels of stability and reliability."]
            if self.A2Q22 in options: # ready
                R2+=["Plan fault tolerance via, e.g., a duplicated system or another parallel system (AI-based or conventional)."]
            if self.A2Q23 in options: # ready
                R2+=["Develop a mechanism to evaluate when the AI system has been changed enough to merit a new review of its technical robustness and safety.Develop a mechanism to evaluate when the AI system has been changed enough to merit a new review of its technical robustness and safety."]
            if self.A2Q27 in options: #ready
                R2+=["Put in place measures to ensure that the data (including training data) used to develop the AI system is up to date, of high quality, complete and representative of the environment the system will be deployed in."]
            if self.A2Q28 in options: #ready
                R2+=["Put in place a series of steps to monitor and document the AI system’s accuracy."]
            if self.A2Q29 in options: # ready
                R2+=["Consider whether the AI system's operation can invalidate the data or assumptions it was trained on, and how this might lead to adversarial effects (e.g. biased estimators, echo chambers etc.)"]
            if self.A2Q30 in options: # ready
                R2+=["Put in place processes to ensure that the level of accuracy of the AI system to be expected by end-users and/or subjects is properly communicated."]
            if self.A2Q34 in options: # ready
                R2+=["Put in place a well-defined process to monitor if the AI system is meeting the goals of the intended applications."]
            if self.A2Q35 in options: #ready
                R2+=["Test whether specific contexts or conditions need to be taken into account to ensure reproducibility."]
            if self.A2Q36 in options: # ready
                R2+=["Put in place verification and validation methods and documentation (e.g. logging) to evaluate and ensure different aspects of the system’s reliability and reproducibility."]
            if self.A2Q37 in options: # ready
                R2+=["Clearly document and operationalize processes for the testing and verification of the reliability and reproducibility of the AI system."]
            if self.A2Q38 in options: #ready
                R2+=["Define tested failsafe fallback plans to address AI system errors of whatever origin and put governance procedures in place to trigger them."]
            if self.A2Q39 in options: #ready
                R2+=["Put in place a proper procedure for handling the cases where the AI system yields results with a low confidence score."]
            if self.A2Q41 in options: #ready
                R2+=["Consider potential negative consequences from the AI system learning novel or unusual methods to score well on its objective function."]
            self.R2=R2
        else:
            self.status2 = False
            self.R2=[]

        if all([elem != 'Unspecified' for elem in list3]):
            self.status3 = True
            if self.A3Q1 in options: #ready
                R3+=["Take measures to consider the impact of the AI system on the right to privacy, the right to physical, mental and/or moral integrity and the right to data protection."]
            if self.A3Q2 in options: #ready
                R3+=["Consider establishing mechanisms that allow flagging issues related to privacy or data protection concerning the AI system."]
            if self.A3Q5 in options: #ready
                R3+=["When relevant, implement the right to withdraw consent, the right to object and the right to be forgotten in the AI system."]
            if self.A3Q6 in options: #ready
                R3+=["Consider the privacy and data protection implications of data collected, generated or processed over the course of the AI system's lifecycle."]
            if self.A3Q7 in options: #ready
                R3+=["Consider the privacy and data protection implications of the AI system's non-personal training-data or other processed non-personal data."]
            if self.A3Q8 in options: #ready
                R3+=["Whenever possible and relevant, align the AI-system with relevant standards (e.g. ISO, IEEE) or widely adopted protocols for (daily) data management and governance."]
            self.R3=R3
        else:
            self.status3 = False
            self.R3=[]

        if all([elem != 'Unspecified' for elem in list4]):
            self.status4 = True
            if self.A4Q1 in options: #ready
                R4+=["Consider adopting measures to continuously assess the quality of the input data to the AI system."]
            if self.A4Q2 in options: #ready
                R4+=["Consider adopting measures to ensure that you can trace back which data was used by the AI system to make a certain decision or recommendation?"]
            if self.A4Q4 in options: # ready
                R4+=["Consider ensuring that you can trace back which AI model/rules led to the decision or recommendation of the AI system."]
            if self.A4Q6 in options: # ready
                R4+=["Consider putting in place adequate logging practices to record the decision(s) or recommendation(s) of the AI system."]
            if self.A4Q8 in options: # ready
                R4+=["Consider explaining the decision adopted or suggested by the AI system to its end users."]
            if self.A4Q10 in options: #ready
                R4+=["Consider continuously surveying the users to ask them whether they understand the decision(s) of the AI system."]
            if self.A4Q11 in options: #ready
                R4+=["In case of interactive AI system, consider communicating to users that they are interacting with a machine."]
            if self.A4Q12 in options: #ready
                R4+=["Consider informing users about the purpose, criteria and limitations of the decision(s) generated by the AI system."]
            if self.A4Q14 in options: #ready
                R4+=["Consider communicating the technical limitations and potential risks of the AI system to end-users, such as its level of accuracy and/or error rates."]
            if self.A4Q16 in options: #ready
                R4+=["Consider providing appropriate training material and disclaimers to users on how to adequately use the AI system."]
            self.R4=R4
        else:
            self.status4 = False
            self.R4=[]

        if all([elem != 'Unspecified' for elem in list5]):
            self.status5 = True
            if self.A5Q1 in options: #ready
                R5+=["Consider establishing a strategy or a set of procedures to avoid creating or reinforcing unfair bias in the AI system, both regarding the use of input data as well as for the algorithm design. "]
            if self.A5Q2 in options: #ready
                R5+=["Consider diversity and representativeness of end-users and/or subjects in the data."]
            if self.A5Q3 in options: #ready
                R5+=["Test for specific target groups or problematic use cases."]
            if self.A5Q4 in options: #ready
                R5+=["Research and use publicly available technical tools, that are state-of-the-art, to improve your understanding of the data, model and performance."]
            if self.A5Q5 in options: #ready
                R5+=["Assess and put in place processes to test and monitor for potential biases during the entire lifecycle of the AI system (e.g. biases due to possible limitations stemming from the composition of the used data sets (lack of diversity, non-representativeness)."]
            if self.A5Q6 in options: #ready
                R5+=["Consider diversity and representativeness of end-users and or subjects in the data."]
            if self.A5Q7 in options: #ready
                R5+=["Put in place educational and awareness initiatives to help AI designers and AI developers be more aware of the possible bias they can inject in designing and developing the AI system."]
            if self.A5Q8 in options: #ready
                R5+=["Depending on the use case, ensure a mechanism that allows for the flagging of issues related to bias, discrimination or poor performance of the AI system."]
            if self.A5Q9 in options:
                R5+=["You should establish clear steps and ways of communicating on how and to whom such issues can be raised."]
            if self.A5Q10 in options:
                R5+=["Identify the subjects that could potentially be (in)directly affected by the AI system, in addition to the (end)-users."]
            if self.A5Q11 in options: #ready
                R5+=["Your definition of fairness should be commonly used and should be implemented in any phase of the process of setting up the AI system."]
            if self.A5Q13 in options: #ready
                R5+=["Consider other definitions of fairness before choosing one."]
            if self.A5Q14 in options:
                R5+=["Consult with the impacted communities about the correct definition of fairness, such as representatives of elderly persons or persons with disabilities."]
            if self.A5Q15 in options:
                R5+=["Ensure a quantitative analysis or metrics to measure and test the applied definition of fairness."]
            if self.A5Q16 in options: #ready
                R5+=["Establish mechanisms to ensure fairness in your AI system."]
            if self.A5Q18 in options:
                R5+=["You should ensure that the AI system corresponds to the variety of preferences and abilities in society."]
            if self.A5Q19 in options:
                R5+=["You should assess whether the AI system's user interface is usable by those with special needs or disabilities or those at risk of exclusion."]
            if self.A5Q20 in options:
                R5+=["You should ensure that information about, and the user interface of, the AI system is accessible and usable also to users of assistive technologies (such as screenreaders)."]
            if self.A5Q21 in options:
                R5+=["You should involve or consult with end-users or subjects in need for assistive technology during the planning and development phase of the AI system."]
            if self.A5Q22 in options:
                R5+=["You should ensure that Universal Design principles are taken into account during every step of the planning and development process, if applicable."]
            if self.A5Q23 in options:
                R5+=["You should take the impact of the AI system on the potential end-users and/or subjects into account."]
            if self.A5Q24 in options:
                R5+=["You should assess whether the team involved in building the AI system engaged with the possible target end-users and/or subjects."]
            if self.A5Q25 in options:
                R5+=["You should assess whether there could be groups who might be disproportionately affected by the outcomes of the system."]
            if self.A5Q27 in options:
                R5+=["You should assess the risk of the possible unfairness of the system onto the end-user's or subject's communities."]
            if self.A5Q30 in options: #ready
                R5+=["You should consider a mechanism to include the participation of the widest range of possible stakeholders in the AI system’s design and development."]
            self.R5=R5
        else:
            self.status5 = False
            self.R5=[]

        if all([elem != 'Unspecified' for elem in list6]):
            self.status6 = True
            if self.A6Q3 in options:
                R6+=["Consider the potential positive and negative impacts of your AI system on the environment and establish mechanisms to evaluate this impact."]
            if self.A6Q5 in options:
                R6+=["Define measures to reduce the environmental impact of your AI system’s lifecycle and participate in competitions for the development of AI solutions that tackle this problem."]
            if self.A6Q10 in options:
                R6+=["Inform and consult with the impacted workers and their representatives but also involve other stakeholders. Implement communication, education, and training at operational and management level."]
            if self.A6Q11 in options:
                R6+=["Take measures to ensure that the work impacts of the AI system are well understood on the basis of an analysis of the work processes and the whole socio-technical system."]
            if self.A6Q14 in options:
                R6+=["Take measures to counteract de-skilling by means of continuous training, especially in areas sensitive in terms of safety and security."]
            if self.A6Q11 in options or self.A6Q19 in options:
                R6+=["Communicate the capabilities but also the limitations of the AI system to end-users, including the level of accuracy of the system."]
            if self.A6Q16 in options:
                R6+=["Provide training opportunities and materials for re- and up-skilling measures."]
            self.R6=R6
        else:
            self.status6 = False
            self.R6=[]

        if all([elem != 'Unspecified' for elem in list7]):
            self.status7 = True
            if self.A7Q1 in options:
                R7+=["Designing a system in a way that can be audited later, results in a more modular and robust system architecture. Thus, it is highly recommended to ensure modularity, traceability of the control and data flow and suitable logging mechanisms."]
            if self.A7Q2 in options:
                R7+=["To facilitate 3rd party auditing can contribute to generate trust in the technology and the product itself. Additionally, it is a strong indication of applying due care in the development and adhering to best practices and industrial standards."]
            if self.A7Q1 in options:
                R7+=["Designing a system in a way that can be audited later, results in a more modular and robust system architecture. Thus, it is highly recommended to ensure modularity, traceability of the control and data flow and suitable logging mechanisms."]
            if self.A7Q2 in options: #ready
                R7+=["To facilitate 3rd party auditing can contribute to generate trust in the technology and the product itself. Additionally, it is a strong indication of applying due care in the development and adhering to best practices and industrial standards."]
            if self.A7Q4 in options:
                R7+=["To foresee 3rd party auditing or guidance can help with both, qualitative and quantitative risk analysis.  In addition, it can contribute to generate trust in the technology and the product itself."]
            if self.A7Q5 in options:
                R7+=["Ensure the involvement of third parties involved in the auditing and evaluation process beyond the development phase."]
            if self.A7Q6 in options:
                R7+=["AI systems should be developed with a preventative approach to risks and in a manner such that they reliably behave as intended while minimising unintentional and unexpected harm, and preventing unacceptable harm. Consequently, developers and deployers should receive appropriate training about the legal framework that applies for the deployed systems."]
            if self.A7Q7 in options:
                R7+=["A useful non-technical method to ensure the implementation of trustworthy AI is to include various stakeholders, e.g. assembled in an “ethical review board” to monitor and assist the development process."]
            if self.A7Q4 in options: #ready
                R7+=["To foresee 3rd party auditing or guidance can help with both, qualitative and quantitative risk analysis.  In addition, it can contribute to generate trust in the technology and the product itself."]
            if self.A7Q8 in options or self.A7Q9  in options:
                R7+=["If AI systems are increasingly used for decision support or for taking decisions themselves, it has to be made sure these systems are fair in their impact on people’s lives, that they are in line with values that should not be compromised and able to act accordingly, and that suitable accountability processes can ensure this. Consequently, all conflicts of values, or trade-offs  should be well documented and explained"]
            if self.A7Q10 in options:
                R7+=["The presence of an internal or external ethical  expert or board might be useful to highlight areas of potential conflict and suggest ways in which that conflict might best resolved. Meaningful consultation and discussion with stakeholders, including those at risk of being adversely affected by an AI system could help as well."]
            if self.A7Q11 in options:
                R7+=["Involving third parties to report on vulnerabilities and risks does help to identify and mitigate potential pitfalls"]
            if self.A7Q12 in options:
                R7+=["A risk management process should always include new findings since initial assumptions about the likelihood of occurrence for a specific risk might be faulty and thus, the quantitative risk analysis was not correct and should be revised with the new findings."]
            if self.A2Q13 in options:
                R7+=["Acknowledging that redress is needed when incorrect predictions  can cause adverse impacts to individuals  is key to ensure trust. Particular attention should be paid to vulnerable persons or groups."]
            self.R7=R7
        else:
            self.status7 = False
            self.R7=[]
        self.last_modified = datetime.datetime.today()
        super(Assessment,self).save()


