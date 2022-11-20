from random import choices
from django import forms
from .models import Assessment, FailureMode, Taiprm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple, widgets, ModelForm, formset_factory

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)
        widgets = {
            'username' : forms.TextInput(attrs={'class':'input'}),
            'email' : forms.EmailInput(attrs={'class':'input'}),
            'password1' : forms.PasswordInput(attrs={'class':'input'}),
            'password2' : forms.PasswordInput(attrs={'class':'input'}),
        }

class AltaiForm(ModelForm):
    class Meta:
        model = Assessment # with wat model you want to work
        fields = ('title','User_domain','AI_domain','AI_status','User_Information')
        exclude = ('author',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'input','placeholder':'title'}), # top set an input format with bootstrap form
        }

class AltaiForm2(ModelForm):
    class Meta:
        model = Assessment # with wat model you want to work
        taiprm = Taiprm # if it is linked to taiprm
        fields = ('title','User_domain','AI_domain','AI_status','User_Information')
        exclude = ('author',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'input','placeholder':'title'}), # top set an input format with bootstrap form
        }

class NotesForm(ModelForm):
    class Meta:
        model = Assessment
        fields = ('notes',)

class TaiprmForm(ModelForm):
    class Meta:
        model = Taiprm # with wat model you want to work
        fields = ('title','User_domain','AI_domain','AI_status','User_Information')
        exclude = ('author',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'input','placeholder':'title'}), # top set an input format with bootstrap form
        }

class NewFailureModeForm(ModelForm):
    class Meta:
        model = FailureMode # with wat model you want to work
        fields = ('name','explanation','driver',)
        exclude = ('author','S','O','D','FailureModeRatio')
        widgets = {
            'name': forms.Textarea(attrs={'class':'input','placeholder':'Name for your failure mode'}), # top set an input format with bootstrap form
            'explanation': forms.Textarea(attrs={'class':'input','placeholder':'Provide some exemplification for other to understand'}),
            'driver': forms.Textarea(attrs={'class':'input','placeholder':'driver from your Failure Mode'}),
        }


class Notes2Form(ModelForm):
    class Meta:
        model = Taiprm
        fields = ('notes',)



class   EditForm1(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['A1Q1','A1Q2','A1Q3','A1Q4','A1Q5','A1Q6','A1Q7','A1Q8','A1Q9','A1Q10',
        'A1Q11','A1Q12','A1Q13','A1Q14','A1Q15','A1Q16','A1Q17','A1Q18','A1Q19','A1Q20',
        'A1Q21','A1Q22','A1Q23','A1Q24','A1Q25','A1Q26','A1Q27','A1Q28','A1Q29','A1Q30','A1Q31','A1Q32',
        'A1Q1_2','A1Q2_2','A1Q3_2','A1Q4_2','A1Q5_2','A1Q6_2','A1Q7_2','A1Q9_2','A1Q10_2',
        'A1Q12_2','A1Q13_2','A1Q14_2','A1Q17_2','A1Q19_2','A1Q21_2','A1Q23_2','A1Q24_2','A1Q25_2','A1Q27_2','A1Q28_2','A1Q29_2','A1Q30_2','A1Q31_2','A1Q32_2',] #
        widgets = {
            'A1Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q8' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A1Q9' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q10' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q11' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A1Q12' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q13' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q14' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q15' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q16' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q17' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q18' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A1Q19' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q20' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A1Q21' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q22' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A1Q23' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q24' : forms.RadioSelect(attrs={'class':'input'}),
           #'A1Q25' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A1Q26' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A1Q27' : forms.RadioSelect(attrs={'class':'input'}),#
            'A1Q28' : forms.RadioSelect(attrs={'class':'input'}),#
            'A1Q29' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q30' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q31' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q32' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q9_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q12_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q13_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q14_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q17_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q19_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q21_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q23_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q24_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q25_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q27_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q28_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q29_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q30_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q31_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A1Q32_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   EditForm2(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['A2Q1','A2Q2','A2Q3','A2Q4','A2Q5','A2Q6','A2Q7','A2Q8','A2Q9','A2Q10',
        'A2Q11','A2Q12','A2Q13','A2Q14','A2Q15','A2Q16','A2Q17','A2Q18','A2Q19','A2Q20',
        'A2Q21','A2Q22','A2Q23','A2Q24','A2Q25','A2Q26','A2Q27','A2Q28','A2Q29','A2Q30',
        'A2Q31','A2Q32','A2Q33','A2Q34','A2Q35','A2Q36','A2Q37','A2Q38','A2Q39','A2Q40',
        'A2Q41','A2Q42','A2Q43','A2Q44','A2Q45','A2Q46',
        'A2Q1_2','A2Q2_2','A2Q3_2','A2Q4_2','A2Q5_2','A2Q7_2','A2Q8_2','A2Q10_2',
        'A2Q11_2','A2Q12_2','A2Q13_2','A2Q14_2','A2Q16_2','A2Q17_2','A2Q18_2','A2Q19_2','A2Q20_2',
        'A2Q21_2','A2Q22_2','A2Q23_2','A2Q24_2','A2Q25_2','A2Q26_2','A2Q27_2','A2Q28_2','A2Q29_2','A2Q30_2',
        'A2Q31_2','A2Q32_2','A2Q33_2','A2Q34_2','A2Q35_2','A2Q36_2','A2Q37_2','A2Q38_2','A2Q39_2','A2Q40_2',
        'A2Q41_2','A2Q42_2','A2Q43_2','A2Q44_2','A2Q45_2','A2Q46_2']
        widgets = {
            'A2Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q6' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A2Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q9' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A2Q10' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q11' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q12' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q13' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q14' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q15' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A2Q16' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q17' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q18' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q19' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q20' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q21' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q22' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q23' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q24' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q25' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q26' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q27' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q28' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q29' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q30' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q31' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q32' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q33' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q34' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q35' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q36' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q37' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q38' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q39' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q40' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q41' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q42' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q43' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q44' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q45' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q46' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q11_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q12_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q13_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q14_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q16_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q17_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q18_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q19_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q20_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q21_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q22_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q23_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q24_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q25_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q26_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q27_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q28_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q29_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q30_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q31_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q32_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q33_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q34_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q35_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q36_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q37_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q38_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q39_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q40_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q41_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q42_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q43_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q44_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q45_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A2Q46_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   EditForm3(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['A3Q1','A3Q2','A3Q3','A3Q4','A3Q5','A3Q6','A3Q7','A3Q8','A3Q9',
        'A3Q1_2','A3Q2_2','A3Q3_2','A3Q4_2','A3Q5_2','A3Q6_2','A3Q7_2','A3Q8_2','A3Q9_2']
        widgets = {
            'A3Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q3' : forms.RadioSelect(attrs={'class':'input'}),
        #    'A3Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q9' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A3Q9_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   EditForm4(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['A4Q1','A4Q2','A4Q3','A4Q4','A4Q5','A4Q6','A4Q7','A4Q8','A4Q9','A4Q10','A4Q11','A4Q12','A4Q13','A4Q14','A4Q15','A4Q16','A4Q17','A4Q18',
        'A4Q1_2','A4Q2_2','A4Q4_2','A4Q6_2','A4Q8_2','A4Q10_2','A4Q11_2','A4Q12_2','A4Q14_2','A4Q16_2','A4Q18_2'] #
        widgets = {
            'A4Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q3' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A4Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q5' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A4Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q7' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A4Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q9' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A4Q10' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q11' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q12' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q13' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A4Q14' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q15' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A4Q16' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q17' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A4Q18' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q11_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q12_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q14_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q16_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A4Q18_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   EditForm5(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['A5Q1','A5Q2','A5Q3','A5Q4','A5Q5','A5Q6','A5Q7','A5Q8','A5Q9','A5Q10',
        'A5Q11','A5Q12','A5Q13','A5Q14','A5Q15','A5Q16','A5Q17','A5Q18','A5Q19','A5Q20',
        'A5Q21','A5Q22','A5Q23','A5Q24','A5Q25','A5Q26','A5Q27','A5Q28','A5Q29','A5Q30','A5Q31',
        'A5Q1_2','A5Q2_2','A5Q3_2','A5Q4_2','A5Q5_2','A5Q6_2','A5Q7_2','A5Q8_2','A5Q9_2','A5Q10_2',
        'A5Q11_2','A5Q13_2','A5Q14_2','A5Q15_2','A5Q16_2','A5Q17_2','A5Q18_2','A5Q19_2','A5Q20_2',
        'A5Q21_2','A5Q22_2','A5Q23_2','A5Q24_2','A5Q25_2','A5Q27_2','A5Q29_2','A5Q30_2','A5Q31_2'
        ] 
        widgets = {
            'A5Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q9' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q10' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q11' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q12' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A5Q13' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q14' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q15' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q16' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q17' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q18' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q19' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q20' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q21' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q22' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q23' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q24' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q25' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q26' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A5Q27' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q28' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A5Q29' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q30' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q31' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q9_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q11_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q13_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q14_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q15_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q16_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q17_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q18_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q19_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q20_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q21_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q22_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q23_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q24_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q25_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q27_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q29_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q30_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A5Q31_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   EditForm6(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['A6Q1','A6Q2','A6Q3','A6Q4','A6Q5','A6Q6','A6Q7','A6Q8','A6Q9','A6Q10','A6Q11',
        'A6Q12','A6Q13','A6Q14','A6Q15','A6Q16','A6Q17','A6Q18','A6Q19','A6Q20',
        'A6Q1_2','A6Q3_2','A6Q5_2','A6Q7_2','A6Q8_2','A6Q9_2','A6Q10_2','A6Q11_2',
        'A6Q13_2','A6Q14_2','A6Q16_2','A6Q17_2','A6Q18_2','A6Q19_2'] #
        widgets = {
            'A6Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q2' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A6Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q4' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A6Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q6' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A6Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q9' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q10' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q11' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q12' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A6Q13' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q14' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q15' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A6Q16' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q17' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q18' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q19' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q20' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'A6Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q9_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q11_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q13_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q14_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q16_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q17_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q18_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A6Q19_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   EditForm7(forms.ModelForm):
      class Meta:
        model = Assessment
        fields = ['A7Q1','A7Q2','A7Q3','A7Q4','A7Q5','A7Q6','A7Q7','A7Q8','A7Q9','A7Q10','A7Q11','A7Q12','A7Q13','A7Q14',
        'A7Q1_2','A7Q2_2','A7Q3_2','A7Q4_2','A7Q5_2','A7Q6_2','A7Q7_2','A7Q8_2','A7Q9_2','A7Q10_2','A7Q11_2','A7Q12_2','A7Q13_2','A7Q14_2'] #
        widgets = {
            'A7Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q9' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q10' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q11' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q12' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q13' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q14' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q9_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q11_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q12_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q13_2' : forms.RadioSelect(attrs={'class':'input'}),
            'A7Q14_2' : forms.RadioSelect(attrs={'class':'input'}),
        }



####################################### end Altai Initial TAI PRM #########
class   Step1Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        fields = ['T1Q1','T1Q2','T1Q3','T1Q4','T1Q5','T1Q6','T1Q7',
        'T1Q1_2','T1Q2_2','T1Q3_2','T1Q4_2','T1Q5_2','T1Q6_2','T1Q7_2'] #
        widgets = {
            'T1Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T1Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   Step2Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        fields = ['T2Q1','T2Q2','T2Q3','T2Q4','T2Q5','T2Q6','T2Q7','T2Q8','T2Q9','T2Q10','intrinsic_risk',
        'T2Q11','T2Q12','T2Q13','T2Q14','T2Q15','T2Q16','T2Q17','T2Q18','T2Q19','T2Q20',
        'T2Q21','T2Q22','T2Q23','T2Q24','T2Q25','T2Q26','T2Q27','T2Q28','T2Q29','T2Q30',
        'T2Q31','T2Q32','T2Q33','T2Q34','T2Q35','T2Q36','T2Q37','T2Q38','T2Q39','T2Q40','T2Q41','T2Q42','T2Q43',
        'T2Q1_2','T2Q2_2','T2Q3_2','T2Q4_2','T2Q5_2','T2Q6_2','T2Q7_2','T2Q8_2','T2Q9_2','T2Q10_2',
        'T2Q11_2','T2Q13_2','T2Q14_2','T2Q15_2','T2Q16_2','T2Q17_2','T2Q18_2','T2Q19_2','T2Q20_2',
        'T2Q21_2','T2Q22_2','T2Q23_2','T2Q24_2','T2Q25_2','T2Q26_2','T2Q27_2','T2Q28_2','T2Q29_2','T2Q30_2',
        'T2Q31_2','T2Q33_2','T2Q34_2','T2Q35_2','T2Q36_2','T2Q37_2','T2Q39_2','T2Q41_2','T2Q42_2'] #
        widgets = {
            'intrinsic_risk' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q9' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q10' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q11' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q12' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'T2Q13' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q14' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q15' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q16' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q17' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q18' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q19' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q20' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q21' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q22' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q23' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q24' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q25' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q26' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q27' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q28' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q29' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q30' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q31' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q32' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'T2Q33' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q34' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q35' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q36' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q37' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q38' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'T2Q39' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q40' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'T2Q41' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q42' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q43' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),

            'T2Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q9_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q11_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q13_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q14_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q15_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q16_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q17_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q18_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q19_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q20_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q21_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q22_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q23_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q24_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q25_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q26_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q27_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q28_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q29_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q30_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q31_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q33_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q34_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q35_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q36_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q37_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q39_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q41_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T2Q42_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   Step3Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        fields = ['T3Q1','T3Q2','T3Q3','T3Q4','T3Q5','T3Q6','T3Q7','T3Q8','T3Q9','T3Q10','T3Q11','T3Q12','T3Q13','T3Q14','T3Q15','T3Q16','T3Q17',
        'T3Q1_2','T3Q2_2','T3Q3_2','T3Q4_2','T3Q5_2','T3Q6_2','T3Q7_2','T3Q8_2','T3Q9_2','T3Q10_2','T3Q12_2','T3Q13_2','T3Q14_2','T3Q15_2','T3Q17_2'] #
        widgets = {
            'T3Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q9' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q10' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q11' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'T3Q12' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q13' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q14' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q15' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q16' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),

            'T3Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q9_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q12_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q13_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q14_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q15_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T3Q17_2' : forms.RadioSelect(attrs={'class':'input'}),

        }

class   Step4Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        fields = ['T4Q1','T4Q2','T4Q3','T4Q4','T4Q5','T4Q6','T4Q7','T4Q8','T4Q9','T4Q10',
        'T4Q1_2','T4Q2_2','T4Q3_2','T4Q4_2','T4Q5_2','T4Q6_2','T4Q7_2','T4Q8_2','T4Q9_2','T4Q10_2'] #
        widgets = {
            'T4Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q6' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q7' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q8' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q9' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q10' : forms.RadioSelect(attrs={'class':'input'}),

            'T4Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q2_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q5_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q6_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q7_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q8_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q9_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T4Q10_2' : forms.RadioSelect(attrs={'class':'input'}),
        }

class   Step5Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        FailureModes = forms.ModelMultipleChoiceField(queryset=FailureMode.objects.all())
        fields = ['FailureModes','T5Q1','T5Q1_2']
        widgets = {
            'FailureModes' : CheckboxSelectMultiple(),
            'T5Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T5Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            
        }




class   Step6Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        FailureModes = forms.ModelMultipleChoiceField(queryset=FailureMode.objects.all())
        fields = ['FailureModes','T6Q1','T6Q1_2','T6Q2']
        widgets = {
            'FailureModes' : CheckboxSelectMultiple(),
            'T6Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T6Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T6Q2' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
        }

class   Step7Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        FailureModes = forms.ModelMultipleChoiceField(queryset=FailureMode.objects.all())
        fields = ['FailureModes','T7Q1','T7Q1_2','T7Q2'] #
        widgets = {
            'FailureModes' : CheckboxSelectMultiple(),
            'T7Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T7Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T7Q2' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
        }

class   Step8Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        FailureModes = forms.ModelMultipleChoiceField(queryset=FailureMode.objects.all())
        fields = ['FailureModes','T8Q1','T8Q1_2','T8Q2'] #
        widgets = {
            'FailureModes' : CheckboxSelectMultiple(),
            'T8Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T8Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T8Q2' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
        }
class   Step9Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        FailureModes = forms.ModelMultipleChoiceField(queryset=FailureMode.objects.all())
        fields = ['FailureModes','T9Q1','T9Q1_2','T9Q2','T9Q3','T9Q4','T9Q5','T9Q3_2','T9Q4_2','T9Q5_2']
        widgets = {
            'FailureModes' : CheckboxSelectMultiple(),
            'T9Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T9Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T9Q2' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'T9Q3' : forms.RadioSelect(attrs={'class':'input'}),
            'T9Q3_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T9Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'T9Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T9Q5' : forms.RadioSelect(attrs={'class':'input'}),
            'T9Q5_2' : forms.RadioSelect(attrs={'class':'input'}),

        }

class   Step10Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        FailureModes = forms.ModelMultipleChoiceField(queryset=FailureMode.objects.all())
        fields = ['FailureModes','T10Q1','T10Q1_2','T10Q2'] #
        widgets = {
            'FailureModes' : CheckboxSelectMultiple(),
            'T10Q1' : forms.RadioSelect(attrs={'class':'input'}),
            'T10Q1_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T10Q2' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
        }

class   Step11Form(forms.ModelForm):
      class Meta:
        model = Taiprm
        FailureModes = forms.ModelMultipleChoiceField(queryset=FailureMode.objects.all())
        fields = ['FailureModes','T11Q4','T11Q4_2','T11Q5','R2_1','R2_2','R2_3','R3_1','R3_2','R3_3','R4_1','R4_2','R4_3',] #
        widgets = {
            'FailureModes' : CheckboxSelectMultiple(),
            'T11Q4' : forms.RadioSelect(attrs={'class':'input'}),
            'T11Q4_2' : forms.RadioSelect(attrs={'class':'input'}),
            'T11Q5' : forms.Textarea(attrs={'class':'form-control','rows':'5'}),
        }


class   PostForm(forms.ModelForm): # form is to specify the widgets .... the style and not  for specifying the conectivity or analysis of information....this is done in views as a class now
    # This is not needed if used static filds!!!!!!!!!!!! this is just an example!!!!!!!!!!!!!!
    class Meta:
        model = Assessment
        fields = ['title']
        exclude = ['author'] # exlude the author since is added automatically later on.
        widgets = {'title' : forms.TextInput(attrs={'class':'input'}),
#            'title_tag' : forms.TextInput(attrs={'class':'input'}),
           # 'author' : forms.Select(attrs={'initial'    'class':'input'}),
#            'body' : forms.Textarea(attrs={'class':'input'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = '__all__'


