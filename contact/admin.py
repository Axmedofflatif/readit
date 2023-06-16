from django.contrib import admin

from .models import Cantact


@admin.register(Cantact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'subject')
    search_fields = ('full_name', 'email', 'subject')
