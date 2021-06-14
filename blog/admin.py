from django.contrib import admin
from .models import Article

# Register your models here.


@admin.register(Article)
class ArtcileModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
    
