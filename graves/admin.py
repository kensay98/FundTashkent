from django.contrib import admin
from .models import Graves, News, Page, OurProjects, Memorials


class GravesAdmin(admin.ModelAdmin):
    ordering = ('name', )
    list_display = ('name', 'birthday', 'day_of_death', 'cem', 'have_photo')
    list_display_links = ('name', 'birthday', 'day_of_death', 'cem')
    search_fields = ('name', )

    def cem(self, obj):
        if obj.cemetery == 1:
            return 'Текстиль'
        else:
            return 'Чигатай'
    cem.short_description = 'Кладбище'

admin.site.register(Graves, GravesAdmin)
admin.site.register(News)
admin.site.register(OurProjects)
admin.site.register(Page)
admin.site.register(Memorials)
