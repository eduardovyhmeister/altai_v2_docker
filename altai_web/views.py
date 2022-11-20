from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Assessment, Taiprm, FailureMode # this import the database called event
#from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect, FileResponse # this is to redirect to a specific page after submission
from django.http import HttpResponse # create different responses.
#This is for agination
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import NewFailureModeForm, RegisterForm, AltaiForm, NotesForm, Step1Form, TaiprmForm, Notes2Form, EditForm1, EditForm2, EditForm3, EditForm4, EditForm5, EditForm6, EditForm7, Step1Form, Step2Form, Step3Form, Step4Form, Step5Form, Step6Form, Step7Form, Step8Form, Step9Form,Step10Form,Step11Form
from django.contrib import messages #this allows to create one time messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #this settle wat pagges are required to be loggin in order to access it .. use "@login_required(login_urls='name_of_url')
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import base64
from django.forms import modelformset_factory, inlineformset_factory
import pandas as pd
import io


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


########################### plot function

def get_graph(): #this is a function to embed views with grapbhs automatically from database.
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def make_radar_chart(stats):
    plt.switch_backend('AGG')
    fig=plt.figure(figsize=(5,5))
    attribute_labels=['Human \n Agency and \n Oversight', 'Technical Robustness \n and Safety','Privacy and \n Data Governance', 'Transparency','Diversity, \n non-discrimination \n and Fairness', 'Societal and \n Env. Well-being','Accountaiblity']
    plot_markers =[0,1,2,3,4,5,]
    plot_str_markers=['0','1','2','3','4','5']
    angles = np.linspace(0, 2*np.pi, len(attribute_labels), endpoint=False)
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, attribute_labels)
    ax.tick_params(labelsize=8)
    plt.yticks(plot_markers)
    ax.set_title('Altai')
    ax.grid(True)
    graph = get_graph()
    return graph

def make_trend_chart(df,names,title,ticks):
    plt.switch_backend('AGG')
    fig=plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax = df[names].plot(kind='box',title=title)
    ax.set_xticklabels(ticks)
    #plt.setp(ax, xticks=[np.random.normal(0, std, 100) for std in range(6, 10)], xticklabels=labels)
    graph = get_graph()
    return graph

#################### create new element




###############     register view
def UserRegisterView(request):
    form = RegisterForm

    if request.method == 'POST': 
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request,'registration.html',context)



def UserLoginView(request):

    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')

    context = {}
    return render(request,'login.html',context)



def UserLogout(request):
    logout(request)
    return redirect('login')



###################### hompage and simple URL creation #####################



def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    name="jhon"
    month =month.capitalize()
    #convert month from name to number
    month_number = list(calendar.month_name).index(month)
    cal =HTMLCalendar().formatmonth(year,month_number)


    return render(request,'home.html',{"first_name":name,
                                        "year":year,
                                        "month":month,
                                        "month_number":month_number,
                                        "cal":cal,
                                        })


def HowToAltai(request):
    context = {}
    return render(request,'howToAltai.html',context)

def FundamentalRights(request):
    context = {}
    return render(request,'fundamentalRights.html',context)

def HowToTAIRMP(request):
    context = {}
    return render(request,'howToTAIRMP.html',context)

def About(request):
    context = {}
    return render(request,'about.html',context)



################# altai views


def MyAltais(request):
    altais = Assessment.objects.all().filter(author=request.user)
    context = {'altais':altais}
    return render(request,'Altai/myAltais.html',context)

def MyAltaisCreate(request):
    submitted = False
    if request.method == "POST":
        form=AltaiForm(request.POST)
        if form.is_valid():
            assessment=form.save(commit=False) # this create the form but do not commit it so can be modified
            assessment.author = request.user # modify the form
            assessment.save()
            return HttpResponseRedirect('myAltais') # /add_event?submitted=True
    else:
        form=AltaiForm
        if 'submitted' in request.GET:
            submitted = True
    form=AltaiForm
    return render(request,'Altai/myAltaisCreate.html',{'form':form, 'submitted':submitted})

@login_required
def MyAltaisDelete(request,pk):
    altai = Assessment.objects.get(pk=pk)
    altai.delete()
    return redirect('myAltais')

@login_required
def MyAltaisHome(request,pk):
    altai = Assessment.objects.get(pk=pk)
    form = NotesForm(request.POST or None, instance=altai)
    if form.is_valid():
        form.save()
        return render(request,'Altai/altaiHome.html',{'altai':altai,'form':form})
    return render(request,'Altai/altaiHome.html',{'altai':altai,'form':form})

@login_required
def MyAltaiReq1(request,pk):
    altai = Assessment.objects.get(pk=pk)
    form = EditForm1(request.POST or None, instance=altai)
    if form.is_valid():
        form.save()
        return render(request,'Altai/altaiAssess1.html',{'altai':altai,'form':form})
    return render(request,'Altai/altaiAssess1.html',{'altai':altai,'form':form})

@login_required
def MyAltaiReq2(request,pk):
    altai = Assessment.objects.get(pk=pk)
    form = EditForm2(request.POST or None, instance=altai)
    if form.is_valid():
        form.save()
        return render(request,'Altai/altaiAssess2.html',{'altai':altai,'form':form})
    return render(request,'Altai/altaiAssess2.html',{'altai':altai,'form':form})

@login_required
def MyAltaiReq3(request,pk):
    altai = Assessment.objects.get(pk=pk)
    form = EditForm3(request.POST or None, instance=altai)
    if form.is_valid():
        form.save()
        return render(request,'Altai/altaiAssess3.html',{'altai':altai,'form':form})
    return render(request,'Altai/altaiAssess3.html',{'altai':altai,'form':form})

@login_required
def MyAltaiReq4(request,pk):
    altai = Assessment.objects.get(pk=pk)
    form = EditForm4(request.POST or None, instance=altai)
    if form.is_valid():
        form.save()
        return render(request,'Altai/altaiAssess4.html',{'altai':altai,'form':form})
    return render(request,'Altai/altaiAssess4.html',{'altai':altai,'form':form})

@login_required
def MyAltaiReq5(request,pk):
    altai = Assessment.objects.get(pk=pk)
    form = EditForm5(request.POST or None, instance=altai)
    if form.is_valid():
        form.save()
        return render(request,'Altai/altaiAssess5.html',{'altai':altai,'form':form})
    return render(request,'Altai/altaiAssess5.html',{'altai':altai,'form':form})

@login_required
def MyAltaiReq6(request,pk):
    altai = Assessment.objects.get(pk=pk)
    form = EditForm6(request.POST or None, instance=altai)
    if form.is_valid():
        form.save()
        return render(request,'Altai/altaiAssess6.html',{'altai':altai,'form':form})
    return render(request,'Altai/altaiAssess6.html',{'altai':altai,'form':form})

@login_required
def MyAltaiReq7(request,pk):
    altai = Assessment.objects.get(pk=pk)
    form = EditForm7(request.POST or None, instance=altai)
    if form.is_valid():
        print('correct')
        form.save()
        return render(request,'Altai/altaiAssess7.html',{'altai':altai,'form':form})
    return render(request,'Altai/altaiAssess7.html',{'altai':altai,'form':form})

@login_required
def ResultsPageAltai(request,pk):
    altai = Assessment.objects.get(pk=pk)


    av1=list(map(int,['0' if x=='Unspecified' else x for x in [altai.A1Q12,altai.A1Q13,altai.A1Q23,altai.A1Q24,altai.A1Q32]]))
    av2=list(map(int,['0' if x=='Unspecified' else x for x in [altai.A2Q10,altai.A2Q11,altai.A2Q24,altai.A2Q25,altai.A2Q31,altai.A2Q32,altai.A2Q42,altai.A2Q43,altai.A2Q44,altai.A2Q45,altai.A2Q46]]))
    av3=list(map(int,['0' if x=='Unspecified' else x for x in [altai.A3Q9]]))
    av4=list(map(int,['0' if x=='Unspecified' else x for x in [altai.A4Q18]]))
    av5=list(map(int,['0' if x=='Unspecified' else x for x in [altai.A5Q17,altai.A5Q29,altai.A5Q31]]))
    av6=list(map(int,['0' if x=='Unspecified' else x for x in [altai.A6Q7,altai.A6Q8,altai.A6Q17,altai.A6Q18]]))
    av7=list(map(int,['0' if x=='Unspecified' else x for x in [altai.A7Q3,altai.A7Q14]]))
   
    chart = make_radar_chart([sum(av1)/len(av1),sum(av2)/len(av2),sum(av3)/len(av3),sum(av4)/len(av4),sum(av5)/len(av5),sum(av6)/len(av6),sum(av7)/len(av7)])
    ####################### global analysis

    charts={}
    for k in ['Manufacturing','Aerospace','Communications','Chemical and Pharmaceutical','Consumer, Goods and Retail','Energy and Utilities','Financial services, Banking and Insurance', 'Freight, Logistics and Transportation','Health and Life Sciences','Hospitality and travel','Media, entertainment, and publishing','Technology']:
 
        Sect1=[list(map(lambda x: np.NaN if x == 'Unspecified' else int(x),d.values())) for d in Assessment.objects.filter(User_domain=k).values('A1Q1_2', 'A1Q2_2', 'A1Q3_2', 'A1Q4_2', 'A1Q5_2', 'A1Q6_2', 'A1Q7_2','A1Q9_2','A1Q10_2','A1Q12_2','A1Q13_2','A1Q14_2','A1Q17_2','A1Q19_2','A1Q21_2','A1Q23_2','A1Q24_2','A1Q25_2','A1Q27_2','A1Q28_2','A1Q29_2','A1Q30_2','A1Q31_2','A1Q32_2')]
        Sect2 =[list(map(lambda x: np.NaN if x == 'Unspecified' else int(x),d.values()))  for d in Assessment.objects.filter(User_domain=k).values('A2Q1_2','A2Q2_2','A2Q3_2','A2Q4_2','A2Q5_2','A2Q7_2','A2Q8_2','A2Q10_2','A2Q11_2','A2Q12_2','A2Q13_2','A2Q14_2','A2Q16_2','A2Q17_2','A2Q18_2','A2Q19_2','A2Q20_2','A2Q21_2','A2Q22_2','A2Q23_2','A2Q24_2','A2Q25_2','A2Q26_2','A2Q27_2','A2Q28_2','A2Q29_2','A2Q30_2','A2Q31_2','A2Q32_2','A2Q33_2','A2Q34_2','A2Q35_2','A2Q36_2','A2Q37_2','A2Q38_2','A2Q39_2','A2Q40_2','A2Q41_2','A2Q42_2','A2Q43_2','A2Q44_2','A2Q45_2','A2Q46_2')]
        Sect3=[list(map(lambda x: np.NaN if x == 'Unspecified' else int(x),d.values()))  for d in Assessment.objects.filter(User_domain=k).values('A3Q1_2', 'A3Q2_2', 'A3Q3_2', 'A3Q4_2', 'A3Q5_2', 'A3Q6_2', 'A3Q7_2','A3Q8_2','A3Q9_2')]
        Sect4=[list(map(lambda x: np.NaN if x == 'Unspecified' else int(x),d.values()))  for d in Assessment.objects.filter(User_domain=k).values('A4Q1_2', 'A4Q2_2', 'A4Q4_2', 'A4Q6_2', 'A4Q8_2', 'A4Q10_2', 'A4Q11_2','A4Q12_2','A4Q14_2','A4Q16_2','A4Q18_2')]
        Sect5=[list(map(lambda x: np.NaN if x == 'Unspecified' else int(x),d.values()))  for d in Assessment.objects.filter(User_domain=k).values('A5Q1_2','A5Q2_2','A5Q3_2','A5Q4_2','A5Q5_2','A5Q6_2','A5Q7_2','A5Q8_2','A5Q9_2','A5Q10_2','A5Q11_2','A5Q13_2','A5Q14_2','A5Q15_2','A5Q16_2','A5Q17_2','A5Q18_2','A5Q19_2','A5Q20_2','A5Q21_2','A5Q22_2','A5Q23_2','A5Q24_2','A5Q25_2','A5Q27_2','A5Q29_2','A5Q30_2','A5Q31_2')]
        Sect6=[list(map(lambda x: np.NaN if x == 'Unspecified' else int(x),d.values()))  for d in Assessment.objects.filter(User_domain=k).values('A6Q1_2','A6Q3_2','A6Q5_2','A6Q7_2','A6Q8_2','A6Q9_2','A6Q10_2','A6Q11_2','A6Q13_2','A6Q14_2','A6Q16_2','A6Q17_2','A6Q18_2','A6Q19_2')]
        Sect7=[list(map(lambda x: np.NaN if x == 'Unspecified' else int(x),d.values()))  for d in Assessment.objects.filter(User_domain=k).values('A7Q1_2','A7Q2_2','A7Q3_2','A7Q4_2','A7Q5_2','A7Q6_2','A7Q7_2','A7Q8_2','A7Q9_2','A7Q10_2','A7Q11_2','A7Q12_2','A7Q13_2','A7Q14_2')]        
        
        dfs1=pd.DataFrame(Sect1,columns=['A1Q1_2', 'A1Q2_2', 'A1Q3_2', 'A1Q4_2', 'A1Q5_2', 'A1Q6_2', 'A1Q7_2','A1Q9_2','A1Q10_2','A1Q12_2','A1Q13_2','A1Q14_2','A1Q17_2','A1Q19_2','A1Q21_2','A1Q23_2','A1Q24_2','A1Q25_2','A1Q27_2','A1Q28_2','A1Q29_2','A1Q30_2','A1Q31_2','A1Q32_2']).dropna(axis=0).reset_index(drop=True)
        dfs2=pd.DataFrame(Sect2,columns=['A2Q1_2','A2Q2_2','A2Q3_2','A2Q4_2','A2Q5_2','A2Q7_2','A2Q8_2','A2Q10_2','A2Q11_2','A2Q12_2','A2Q13_2','A2Q14_2','A2Q16_2','A2Q17_2','A2Q18_2','A2Q19_2','A2Q20_2','A2Q21_2','A2Q22_2','A2Q23_2','A2Q24_2','A2Q25_2','A2Q26_2','A2Q27_2','A2Q28_2','A2Q29_2','A2Q30_2','A2Q31_2','A2Q32_2','A2Q33_2','A2Q34_2','A2Q35_2','A2Q36_2','A2Q37_2','A2Q38_2','A2Q39_2','A2Q40_2','A2Q41_2','A2Q42_2','A2Q43_2','A2Q44_2','A2Q45_2','A2Q46_2']).dropna(axis=0).reset_index(drop=True)
        dfs3=pd.DataFrame(Sect3,columns=['A3Q1_2', 'A3Q2_2', 'A3Q3_2', 'A3Q4_2', 'A3Q5_2', 'A3Q6_2', 'A3Q7_2','A3Q8_2','A3Q9_2']).dropna(axis=0).reset_index(drop=True)
        dfs4=pd.DataFrame(Sect4,columns=['A4Q1_2', 'A4Q2_2', 'A4Q4_2', 'A4Q6_2', 'A4Q8_2', 'A4Q10_2', 'A4Q11_2','A4Q12_2','A4Q14_2','A4Q16_2','A4Q18_2']).dropna(axis=0).reset_index(drop=True)
        dfs5=pd.DataFrame(Sect5,columns=['A5Q1_2','A5Q2_2','A5Q3_2','A5Q4_2','A5Q5_2','A5Q6_2','A5Q7_2','A5Q8_2','A5Q9_2','A5Q10_2','A5Q11_2','A5Q13_2','A5Q14_2','A5Q15_2','A5Q16_2','A5Q17_2','A5Q18_2','A5Q19_2','A5Q20_2','A5Q21_2','A5Q22_2','A5Q23_2','A5Q24_2','A5Q25_2','A5Q27_2','A5Q29_2','A5Q30_2','A5Q31_2']).dropna(axis=0).reset_index(drop=True)
        dfs6=pd.DataFrame(Sect6,columns=['A6Q1_2','A6Q3_2','A6Q5_2','A6Q7_2','A6Q8_2','A6Q9_2','A6Q10_2','A6Q11_2','A6Q13_2','A6Q14_2','A6Q16_2','A6Q17_2','A6Q18_2','A6Q19_2']).dropna(axis=0).reset_index(drop=True)
        dfs7=pd.DataFrame(Sect7,columns=['A7Q1_2','A7Q2_2','A7Q3_2','A7Q4_2','A7Q5_2','A7Q6_2','A7Q7_2','A7Q8_2','A7Q9_2','A7Q10_2','A7Q11_2','A7Q12_2','A7Q13_2','A7Q14_2']).dropna(axis=0).reset_index(drop=True)
        print(Sect2)
        if not dfs1.empty:
            chart1 = make_trend_chart(dfs1,['A1Q1_2', 'A1Q2_2', 'A1Q3_2', 'A1Q4_2', 'A1Q5_2', 'A1Q6_2', 'A1Q7_2','A1Q9_2','A1Q10_2','A1Q12_2','A1Q13_2','A1Q14_2','A1Q17_2','A1Q19_2','A1Q21_2','A1Q23_2','A1Q24_2','A1Q25_2','A1Q27_2','A1Q28_2','A1Q29_2','A1Q30_2','A1Q31_2','A1Q32_2'],'Trends for Human Agency and Oversight in '+k,['1', '2', '3', '4', '5', '6', '7','9','10','12','13','14','17','19','21','23','24','25','27','28','29','30','31','32'])
            charts[k+' Human Agency and Oversight']=chart1
        if not dfs2.empty:
            chart2 = make_trend_chart(dfs2,['A2Q1_2','A2Q2_2','A2Q3_2','A2Q4_2','A2Q5_2','A2Q7_2','A2Q8_2','A2Q10_2','A2Q11_2','A2Q12_2','A2Q13_2','A2Q14_2','A2Q16_2','A2Q17_2','A2Q18_2','A2Q19_2','A2Q20_2','A2Q21_2','A2Q22_2','A2Q23_2','A2Q24_2','A2Q25_2','A2Q26_2','A2Q27_2','A2Q28_2','A2Q29_2','A2Q30_2','A2Q31_2','A2Q32_2','A2Q33_2','A2Q34_2','A2Q35_2','A2Q36_2','A2Q37_2','A2Q38_2','A2Q39_2','A2Q40_2','A2Q41_2','A2Q42_2','A2Q43_2','A2Q44_2','A2Q45_2','A2Q46_2'],'Trends for Technical Robustness and Safety in '+k,['1', '2', '3', '4', '5', '7','8','10','11','12','13','14','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46'])
            charts[k+' Technical Robustness and Safety']=chart2
        if not dfs3.empty:
            chart3 = make_trend_chart(dfs3,['A3Q1_2', 'A3Q2_2', 'A3Q3_2', 'A3Q4_2', 'A3Q5_2', 'A3Q6_2', 'A3Q7_2','A3Q8_2','A3Q9_2'],'Trends for Technical Robustness and Safety in '+k,['1', '2', '3', '4', '5', '6','7','8','9'])
            charts[k+' Privacy and Data Governance']=chart3
        if not dfs4.empty:
            chart4 = make_trend_chart(dfs4,['A4Q1_2', 'A4Q2_2', 'A4Q4_2', 'A4Q6_2', 'A4Q8_2', 'A4Q10_2', 'A4Q11_2','A4Q12_2','A4Q14_2','A4Q16_2','A4Q18_2'],'Trends for Technical Robustness and Safety in '+k,['1', '2', '4', '6', '8', '10','11','12','14','16','18'])
            charts[k+' Privacy and Data Governance']=chart4
        if not dfs5.empty:
            chart5 = make_trend_chart(dfs5,['A5Q1_2','A5Q2_2','A5Q3_2','A5Q4_2','A5Q5_2','A5Q6_2','A5Q7_2','A5Q8_2','A5Q9_2','A5Q10_2','A5Q11_2','A5Q13_2','A5Q14_2','A5Q15_2','A5Q16_2','A5Q17_2','A5Q18_2','A5Q19_2','A5Q20_2','A5Q21_2','A5Q22_2','A5Q23_2','A5Q24_2','A5Q25_2','A5Q27_2','A5Q29_2','A5Q30_2','A5Q31_2'],'Trends for Technical Robustness and Safety in '+k,['1', '2','3', '4','5', '6','7', '8','9', '10','11','13','14','15','16','17','18','19','20','21','22','23','24','25','27','29','30','31'])
            charts[k+' Privacy and Data Governance']=chart5
        if not dfs6.empty:
            chart6 = make_trend_chart(dfs6,['A6Q1_2','A6Q3_2','A6Q5_2','A6Q7_2','A6Q8_2','A6Q9_2','A6Q10_2','A6Q11_2','A6Q13_2','A6Q14_2','A6Q16_2','A6Q17_2','A6Q18_2','A6Q19_2'],'Trends for Technical Robustness and Safety in '+k,['1', '3', '5', '7', '8', '9','10','11','13','14','16','17','18','19'])
            charts[k+' Privacy and Data Governance']=chart6
        if not dfs7.empty:
            chart7 = make_trend_chart(dfs7,['A7Q1_2','A7Q2_2','A7Q3_2','A7Q4_2','A7Q5_2','A7Q6_2','A7Q7_2','A7Q8_2','A7Q9_2','A7Q10_2','A7Q11_2','A7Q12_2','A7Q13_2','A7Q14_2'],'Trends for Technical Robustness and Safety in '+k,['1', '2', '3','4','5', '6','7', '8','9', '10','11','12','13','14'])
            charts[k+' Privacy and Data Governance']=chart7

    #######################
    context = {'altai':altai,'chart':chart,'chart2':chart1,'charts':charts,'R1':eval(altai.R1),'R2':eval(altai.R2),'R3':eval(altai.R3),'R4':eval(altai.R4),'R5':eval(altai.R5),'R6':eval(altai.R6),'R7':eval(altai.R7)}
    return render(request,'Altai/altaiResults.html',context)


################# taiprm Views

def MyTaiprm(request):
    taiprm = Taiprm.objects.all().filter(author=request.user)
    context = {'taiprm':taiprm}
    return render(request,'TAI_PRM/myTaiprm.html',context)

def MyTaiprmCreate(request):
    submitted = False
    if request.method == "POST":
        form=TaiprmForm(request.POST)
        if form.is_valid():
            taiprm=form.save(commit=False) # this create the form but do not commit it so can be modified
            taiprm.author = request.user # modify the form
            taiprm.save()
            return HttpResponseRedirect('myTaiprm') # /add_event?submitted=True
    else:
        form=TaiprmForm
        if 'submitted' in request.GET:
            submitted = True
    form=TaiprmForm
    return render(request,'TAI_PRM/myTaiprmCreate.html',{'form':form, 'submitted':submitted})

def NewFailureMode(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    submitted = False
    if request.method == "POST":
        form=NewFailureModeForm(request.POST)
        if form.is_valid():
            failuremode=form.save(commit=False) # this create the form but do not commit it so can be modified
            failuremode.author = request.user # modify the form
            failuremode.save()
             # /add_event?submitted=True
            return render(request,'TAI_PRM/newFailureMode.html',{'form':form, 'submitted':submitted, 'taiprm':taiprm})
    else:
        form=NewFailureModeForm
        if 'submitted' in request.GET:
            submitted = True
    form=NewFailureModeForm
    return render(request,'TAI_PRM/newFailureMode.html',{'form':form, 'submitted':submitted, 'taiprm':taiprm})




def MyTaiprmDelete(request,pk):
    altai = Taiprm.objects.get(pk=pk)
    altai.delete()
    return redirect('myTaiprm')

def MyTaiprmHome(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    form = Notes2Form(request.POST or None, instance=taiprm)
    if form.is_valid():
        form.save()
        return render(request,'TAI_PRM/taiprmHome.html',{'taiprm':taiprm,'form':form})
    return render(request,'TAI_PRM/taiprmHome.html',{'taiprm':taiprm,'form':form})

def MyTaiprmStep1(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    form = Step1Form(request.POST or None, instance=taiprm)
    if form.is_valid():
        form.save()
        return render(request,'TAI_PRM/taiprmStep1.html',{'taiprm':taiprm,'form':form})
    else:
        print('ERROR IN THE FORM STEP 1')
    return render(request,'TAI_PRM/taiprmStep1.html',{'taiprm':taiprm,'form':form})

def MyTaiprmStep2(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    form = Step2Form(request.POST or None, instance=taiprm)
    if form.is_valid():
        form.save()
        return render(request,'TAI_PRM/taiprmStep2.html',{'taiprm':taiprm,'form':form})
    else:
        print('ERROR IN THE FORM STEP 2')
    return render(request,'TAI_PRM/taiprmStep2.html',{'taiprm':taiprm,'form':form})

def MyTaiprmStep3(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    form = Step3Form(request.POST or None, instance=taiprm)
    if form.is_valid():
        form.save()
        return render(request,'TAI_PRM/taiprmStep3.html',{'taiprm':taiprm,'form':form})
    return render(request,'TAI_PRM/taiprmStep3.html',{'taiprm':taiprm,'form':form})

def MyTaiprmStep4(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    form = Step4Form(request.POST or None, instance=taiprm)
    if form.is_valid():
        form.save()
        return render(request,'TAI_PRM/taiprmStep4.html',{'taiprm':taiprm,'form':form})
    return render(request,'TAI_PRM/taiprmStep4.html',{'taiprm':taiprm,'form':form})

def MyTaiprmStep5(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    form = Step5Form(request.POST or None, instance=taiprm)
    ids = eval(taiprm.SelectedFailureModes)
    lista = [True if x+1 in ids else False for x in range(FailureMode.objects.all().count())]
    if request.method == "POST":
        selection =[]
        failuremodes=FailureMode.objects.all().values_list('name',flat=True)
        for j in failuremodes:
            selection+=list(map(int,request.POST.getlist(j)))
        if len(selection)!=len(ids): # this is if there is new selections, they have to run again the process..
            taiprm.status7=False
            taiprm.status8=False
            taiprm.status9=False
        if form.is_valid():
            taiprm.SelectedFailureModes = selection
            taiprm.save()
            form.save()
            return redirect('myTaiprmStep6',pk=pk)
        else:
            return render(request,'TAI_PRM/taiprmStep5.html',{'taiprm':taiprm,'form':form,'ids':ids,'lista':lista})
    return render(request,'TAI_PRM/taiprmStep5.html',{'taiprm':taiprm,'form':form,'ids':ids,'lista':lista})

def MyTaiprmStep6(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    ids = eval(taiprm.SelectedFailureModes)
    selectedFailureModesNames = list(FailureMode.objects.filter(pk__in=ids).values_list('name',flat=True))
    print(selectedFailureModesNames)
    form = Step6Form(request.POST or None, instance=taiprm)
    if request.method == "POST":
        selection=[]
        for j in selectedFailureModesNames:
            id_list = request.POST.getlist(j)
            selection+=list(map(int,id_list))
            print(id_list)
        taiprm.S=selection
        taiprm.save()
        if form.is_valid():
            form.save()
            return redirect('myTaiprmStep7',pk=pk)
        else:
            return render(request,'TAI_PRM/taiprmStep6.html',{'taiprm':taiprm,'form':form,'ids':ids,'range':[1,2,3,4,5,6,7,8,9,10],'lista':eval(taiprm.S)})
    else:
        return render(request,'TAI_PRM/taiprmStep6.html',{'taiprm':taiprm,'form':form,'ids':ids,'range':[1,2,3,4,5,6,7,8,9,10],'lista':eval(taiprm.S)})


def MyTaiprmStep7(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    ids = eval(taiprm.SelectedFailureModes)
    selectedFailureModesNames = list(FailureMode.objects.filter(pk__in=ids).values_list('name',flat=True))
    form = Step7Form(request.POST or None, instance=taiprm)
    if request.method == "POST":
        selection=[]
        for j in selectedFailureModesNames:
            id_list = request.POST.getlist(j)
            selection+=list(map(int,id_list))
        taiprm.O=selection
        taiprm.save()
        if form.is_valid():
            form.save()
            return redirect('myTaiprmStep8',pk=pk)
        else:
            return render(request,'TAI_PRM/taiprmStep7.html',{'taiprm':taiprm,'form':form,'ids':ids,'range':[1,2,3,4,5,6,7,8,9,10]})
    else:
        return render(request,'TAI_PRM/taiprmStep7.html',{'taiprm':taiprm,'form':form,'ids':ids,'range':[1,2,3,4,5,6,7,8,9,10]})

def MyTaiprmStep8(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    ids = eval(taiprm.SelectedFailureModes)
    selectedFailureModesNames = list(FailureMode.objects.filter(pk__in=ids).values_list('name',flat=True))
    form = Step8Form(request.POST or None, instance=taiprm)
    if request.method == "POST":
        selection=[]
        for j in selectedFailureModesNames:
            id_list = request.POST.getlist(j)
            selection+=list(map(int,id_list))
        taiprm.D=selection
        taiprm.save()
        if form.is_valid():
            form.save()
            return redirect('myTaiprmStep9',pk=pk)
        else:
            return render(request,'TAI_PRM/taiprmStep8.html',{'taiprm':taiprm,'form':form,'ids':ids,'range':[1,2,3,4,5,6,7,8,9,10]})
    else:
        return render(request,'TAI_PRM/taiprmStep8.html',{'taiprm':taiprm,'form':form,'ids':ids,'range':[1,2,3,4,5,6,7,8,9,10]})


def MyTaiprmStep9(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    ids = list(map(int,eval(taiprm.SelectedFailureModes)))
    selectedFailureModesNames = list(FailureMode.objects.filter(pk__in=ids).values_list('name',flat=True))
    form = Step9Form(request.POST or None, instance=taiprm)
    if request.method == "POST":
        selection=[]
        for j in selectedFailureModesNames:
            id_list = request.POST.getlist(j)
            selection+=list(map(float,id_list))
        taiprm.alpha=selection
        S=eval(taiprm.S)
        O=eval(taiprm.O)
        D=eval(taiprm.D)
        alpha=taiprm.alpha
        taiprm.RPN = [a*b*c for a,b,c in zip(S,O,D)]
        taiprm.GRPN=np.dot(np.dot(np.dot(S,O),D),alpha)
        taiprm.save()
        if form.is_valid():
            form.save()
            return redirect('myTaiprmStep10',pk=pk)
        else:
            return render(request,'TAI_PRM/taiprmStep9.html',{'taiprm':taiprm,'form':form,'ids':ids})
    else:
        return render(request,'TAI_PRM/taiprmStep9.html',{'taiprm':taiprm,'form':form,'ids':ids})

def MyTaiprmStep10(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    ids = list(map(int,eval(taiprm.SelectedFailureModes)))
    selectedFailureModesNames = list(FailureMode.objects.filter(pk__in=ids).values_list('name',flat=True))
    form = Step10Form(request.POST or None, instance=taiprm)
    if form.is_valid():
        id_list=request.POST.getlist('FailureModes')
        taiprm.SelectedFailureModes = id_list
        taiprm.save()
        form.save()
        return render(request,'TAI_PRM/taiprmStep10.html',{'taiprm':taiprm,'form':form,'ids':ids})
    return render(request,'TAI_PRM/taiprmStep10.html',{'taiprm':taiprm,'form':form,'ids':ids})

def MyTaiprmStep11(request,pk):
    altais = Assessment.objects.all().filter(author=request.user)
    taiprm = Taiprm.objects.get(pk=pk)
    form = Step11Form(request.POST or None, instance=taiprm)
    id_list=request.POST.getlist('altais')
    check=True
    
    #print (request.POST.get('R1_1'))
    #print (altais[int(id_list[0])])
    #if request.POST.get('R1_1')>request.POST.get('R1_2') or request.POST.get('R1_2')>request.POST.get('R1_3') or request.POST.get('R2_1')>request.POST.get('R2_2') or request.POST.get('R2_2')>request.POST.get('R2_3') or request.POST.get('R3_1')>request.POST.get('R3_2') or request.POST.get('R3_2')>request.POST.get('R3_3') or request.POST.get('R4_1')>request.POST.get('R4_2') or request.POST.get('R4_2')>request.POST.get('R4_3'):
    #    check=False
    if form.is_valid():
        if len(id_list)!=0:
            taiprm.altai=altais[int(id_list[0])].id
            print(taiprm.altai)
            thealtai=Assessment.objects.get(pk=taiprm.altai)
            print(thealtai)
        taiprm.save()
        form.save()
        return render(request,'TAI_PRM/taiprmStep11.html',{'taiprm':taiprm,'form':form,'altais':altais})

    return render(request,'TAI_PRM/taiprmStep11.html',{'taiprm':taiprm,'form':form,'altais':altais})


def MyTaiprmResults(request,pk):
    taiprm = Taiprm.objects.get(pk=pk)
    context = {'taiprm':taiprm,'Resp1':eval(taiprm.R1),'Resp2':eval(taiprm.R2),'Resp3':eval(taiprm.R3),'Resp4':eval(taiprm.R4),'Resp5':eval(taiprm.R5),'Resp6':eval(taiprm.R6),'Resp7':eval(taiprm.R7)}
    return render(request,'TAI_PRM/taiprmResults.html',context)


def MyTaiprmPdf(request,pk):

    taiprm = Taiprm.objects.get(pk=pk)
    thealtai=Assessment.objects.get(pk=taiprm.altai)
    ids = list(map(int,eval(taiprm.SelectedFailureModes)))
    selectedFailureModesNames = list(FailureMode.objects.filter(pk__in=ids).values_list('name',flat=True))

    template_path = 'TAI_PRM/user_printer.html'
    context = {'taiprm': taiprm,'thealtai':thealtai,'ids':ids,'selectedFailureModesNames':selectedFailureModesNames}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



######################## examples of update
#def update_venue(request,venue_id): # USE THIS FOR ASSISTANT SINCE INCLUDE UPDATE
#    venue = Venue.objects.get(pk=venue_id) # this is how to get a specific component...in the primary key (pk) is the venue id that comes from the html call
#    form  = VenueForm(request.POST or None, instance=venue) # instance specify the inform from the specific vneu_id
#    if form.is_valid():
#        form.save()
#        return redirect('list_venues')
#    return render(request,'events/update_venue.html',{
#                                    'venue':venue, 'form':form
#                                        })


#def update_event(request,event_id): # USE THIS FOR ASSISTANT SINCE INCLUDE UPDATE
#    event = Event.objects.get(pk=event_id) # this is how to get a specific component...in the primary key (pk) is the venue id that comes from the html call
#    form  = EventForm(request.POST or None, instance=event) # instance specify the inform from the specific vneu_id
#    if form.is_valid():
#        form.save()
#        return redirect('list_event')
#    return render(request,'events/update_event.html',{
#                                    'event':event, 'form':form
#                                        })

########################################### example of search tab


#def search_venue(request):
#    if request.method == "POST":
#        searched = request.POST['BUSQUEDA'] # this look at the input
#        venue =Venue.objects.filter(name__contains=searched) # to search in the data base use doble _ i.e. __
#        return render(request, 'events/search_venues.html',
#        {'searched':searched,'venue':venue})

#    else:
#        return render(request, 'events/search_venues.html',
#        {})