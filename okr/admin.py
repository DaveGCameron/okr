from django.contrib import admin

from okr.models import Company, Employee, Period


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_count')
    def employee_count(self, obj):
        return obj.employee_set.count()
admin.site.register(Company, CompanyAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
admin.site.register(Employee, EmployeeAdmin)

class PeriodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Period, PeriodAdmin)
