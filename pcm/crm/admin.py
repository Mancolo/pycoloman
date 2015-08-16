from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
from .models import Customer, CustomerKind, Contact, RackPosition, Rack, Room, Cage

class RackPositionInline(GenericTabularInline):
  model = RackPosition

class RoomAdmin(admin.ModelAdmin):
  inlines = [ RackPositionInline ]

class CageAdmin(admin.ModelAdmin):
  inlines = [ RackPositionInline ]

admin.site.register(Customer)
admin.site.register(CustomerKind)
admin.site.register(Contact)
admin.site.register(RackPosition)
admin.site.register(Rack)
admin.site.register(Room, RoomAdmin)
admin.site.register(Cage, CageAdmin)
