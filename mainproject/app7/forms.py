from django import forms
from app7.models import Employee
from app7.models import News
from app7.models import Holidays
from django.contrib.auth.models import User

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields='__all__'

class HolidaysForm(forms.ModelForm):
    class Meta:
        model=Holidays
        fields='__all__'        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'    
        
class SignUpForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name']
