from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app7.models import Employee
from app7.forms import EmployeeForm
from app7.models import News
from app7.forms import NewsForm
from app7.models import Holidays
from app7.forms import HolidaysForm
from app7.forms import SignUpForm
from django.http import HttpResponseRedirect
  
# Create your views here.
def newsdata(request):
	newss=News.objects.all()
	return render(request,'app7/newsdata.html',{'n':newss})
def newsform(request):
	form=NewsForm()
	if request.method=="POST":
		form=NewsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/newsdata')
	return render(request,'app7/newsform.html',{'f':form})
def calender(request):
	holidayss=Holidays.objects.all()
	return render(request,'app7/calender.html',{'h':holidayss})

def holiday(request):
	form=HolidaysForm()
	if request.method=="POST":
		form=HolidaysForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/calender')
	return render(request,'app7/holiday.html',{'f':form})


def home(request):
    return render(request,'app7/home.html')
    
@login_required
def hrm(request):
    return render(request,'app7/hrm.html')  
@login_required
def employee(request):
	employees=Employee.objects.all()
	return redirect('/calenderholiday')
	return render(request,'app7/employee.html',{'e':employees})


def base(request):
    return render(request,'app7/base.html') 
def sample_view(request):
	employees=Employee.objects.all()
	return render(request,'app7/sample.html',{'e':employees})
def insert_view(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hrm')

    return render(request,'app7/form.html',{'form':form})
def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/sample')
def update_view(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=="POST":
		form=EmployeeForm(request.POST, instance=employee) #instance=employee means replacing existing record
		if form.is_valid():
			form.save()
		return redirect('/sample') #redirecting to results page like sample.html
	return render(request,'app7/update.html',{'employee':employee})

def calenderholiday(request):
    return render(request,'app7/calenderholiday.html') 

def signup_view(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
		
	return render(request,'app7/signup.html',{'form':form})	
   