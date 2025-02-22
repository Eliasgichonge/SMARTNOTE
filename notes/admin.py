from django.contrib import admin

class NotesAdmin(admin.ModelAdmin):
      pass

admin.site.register(models.Notes, NotesAdmin)
