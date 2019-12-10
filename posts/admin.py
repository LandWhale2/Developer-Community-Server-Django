from django.contrib import admin
from .models import Talk
# Register your models here.

class TalkAdmin(admin.ModelAdmin):
    list_display = ('created',)


admin.site.register(Talk, TalkAdmin)

