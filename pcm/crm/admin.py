from django.contrib import admin

# Register your models here.
from .models import Customer, CustomerKind, Contact


admin.site.register(Customer)
admin.site.register(CustomerKind)
admin.site.register(Contact)
