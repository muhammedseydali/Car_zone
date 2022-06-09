from django.utils.html import format_html
from django.contrib import admin
from pages.models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display= ('id','thumbnail','first_name','last_name','designation','created_date',)

    list_display_links = ('id','thumbnail','first_name',)

    search_fields = ('first_name','last_name','designation',)

    list_filter = ('designation',)
    
    
admin.site.register(Team,TeamAdmin)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'demo',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }