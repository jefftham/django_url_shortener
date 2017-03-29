from django.contrib import admin
from .models import Url_table


class UrlAdmin(admin.ModelAdmin):
    # list the fields of overviews
    list_display = ('pk', 'short', 'count')
    # add search bar
    search_fields = ('short',)


# Register your models here.
admin.site.register(Url_table, UrlAdmin)
