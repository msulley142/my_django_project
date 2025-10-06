from django.contrib import admin
from .models import Dog, Breed

class DogAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'age', 'breed')
   
    search_fields = ('name', 'breed')

    
    list_filter = ('age', 'breed')

   
    list_display_links = ('name',)

   
    fields = ('name', 'age', 'breed')





# Register your models here.
admin.site.register(Dog)
admin.site.register(Breed)