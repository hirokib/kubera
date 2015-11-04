from django.contrib import admin
from mobile.models import Customer, Balance, Transaction


# Register your models here.
admin.site.register(Customer)
admin.site.register(Balance)
admin.site.register(Transaction)