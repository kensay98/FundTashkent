from django.contrib import admin
from .models import Graves, News, Page, OurProjects, Memorials


class GravesAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'sector', 'row', 'number', 'birthday', 'day_of_death', 'cemetery', 'have_photo')
    list_display_links = ('name', 'sector', 'row', 'number', 'birthday', 'day_of_death', 'cemetery', 'have_photo')
    search_fields = ('name',)
    list_filter = ('cemetery', 'sector', 'row', 'number')

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
