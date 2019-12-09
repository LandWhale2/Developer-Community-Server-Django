from django.contrib import admin
from posts.models import Posts
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('created',)


admin.site.register(Posts, PostsAdmin)

