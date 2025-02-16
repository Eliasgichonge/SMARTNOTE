from django.contrib import admin

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created')
