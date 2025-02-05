from django.contrib import admin
from .models import Registration, Activity, Gallery

# Register your models here.
admin.site.register(Registration)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('ActivityName', 'description')
    search_fields = ('ActivityName', 'description')


admin.site.register(Activity, ActivityAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title', 'image')


admin.site.register(Gallery, GalleryAdmin)

