from django.contrib import admin
from .models import Post

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamped"]
    list_filter = ["title"]
    class Meta():
        model=Post

admin.site.register(Post,PostModelAdmin)
