from django.contrib import admin
from myapp38.models import Animal, Visitor, Ticket, Visit


class ZooAdmin(admin.ModelAdmin):
    pass


admin.site.register(Animal)
admin.site.register(Visitor)
admin.site.register(Ticket)
admin.site.register(Visit)