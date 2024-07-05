from django.contrib import admin
from .models import Registration, Activity

# Register your models here.
admin.site.register(Registration)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('ActivityName', 'description')
    search_fields = ('ActivityName', 'description')


admin.site.register(Activity, ActivityAdmin)

