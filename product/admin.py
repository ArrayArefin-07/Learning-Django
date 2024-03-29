from django.contrib import admin
from .models import laptop

# Register your models here.
# admin.site.register(laptop)
#another wat to register your model
@admin.register(laptop) 

class laptopAdmin(admin.ModelAdmin):
    list_display = ('password','re_password','laptop','re_laptop','email',
    'textarea','checkbox','ram','ssd','youtube_chanel')