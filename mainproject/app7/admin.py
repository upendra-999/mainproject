from django.contrib import admin
from app7.models import Employee
from app7.models import News
from app7.models import Holidays
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	list_display=['noccation']
admin.site.register(News, NewsAdmin) 	

class HolidaysAdmin(admin.ModelAdmin):
	list_display=['date','occation']
admin.site.register(Holidays, HolidaysAdmin) 	

class EmployeeAdmin (admin.ModelAdmin):
	list_display=['ename','eid','edes','edate','edept','esal','eexp']

admin.site.register(Employee, EmployeeAdmin)    


