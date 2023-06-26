from django.contrib import admin
from bookapp.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['tital','author','pages','prise']

admin.site.register(Book,BookAdmin)
