from models import Person, Profession, Specialty
from forms import PersonForm

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User




class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title',)

class PersonInline(admin.StackedInline):
    model = Person
    fk_name = 'user'
    max_num = 1

class PersonAdmin(admin.ModelAdmin):
    form = PersonForm

# Will be switched on when the Profile model is activated
#class MediramaUserAdmin(UserAdmin):
#    inlines = [PersonInline,]
    
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Person)
#admin.site.unregister(User)
#admin.site.register(User, MediramaUserAdmin)
    
