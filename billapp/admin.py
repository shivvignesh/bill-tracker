from django.contrib import admin
from billapp.models import Bill,Expense
# Register your models here.
admin.site.register(Bill)
admin.site.register(Expense)