from django.contrib import admin
from .models import CountryImages,  scholars_list, Basicinfo, VisaInformation, Contacts, newScholarship, reviews

# Register your models here.

admin.site.register(CountryImages)
admin.site.register(scholars_list)
admin.site.register(Basicinfo)
admin.site.register(VisaInformation)
admin.site.register(Contacts)
admin.site.register(newScholarship)
admin.site.register(reviews)







