from django.contrib import admin
from .models import Talk, Projects, Algorithm, Skilltalk

# Register your models here.

class TalkAdmin(admin.ModelAdmin):
    list_display = ('content',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('content',)

class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('content',)

class SkilltalkAdmin(admin.ModelAdmin):
    list_display = ('content',)




admin.site.register(Talk, TalkAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(Algorithm, AlgorithmAdmin)
admin.site.register(Skilltalk, SkilltalkAdmin)