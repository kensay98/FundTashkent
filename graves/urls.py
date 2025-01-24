import graves.views
from django.urls import path, re_path


urlpatterns = [
    path('', graves.views.index, name='index'),
    path('news/', graves.views.news_list, name='news'),
    path('partners/', graves.views.partners, name='partners'),
    path('contacts/', graves.views.contacts, name='contacts'),
    path('gallery/', graves.views.gallery, name='gallery'),
    path('about/', graves.views.about, name='about'),
    path('donate/', graves.views.donate, name='donate'),
    path('search/', graves.views.graves_search, name='search'),
    re_path(r'^cemetery/(?P<cem_id>\d+)/$', graves.views.graves_list, name='graves'),
    re_path(r'^cemetery/(?P<cem_id>\d+)/(?P<letter>\S)/$', graves.views.graves_list, name='graves'),
    re_path(r'^grave/(?P<grave_id>\d+)/$', graves.views.graves_detail, name='grave'),
    re_path(r'^page/(?P<title>\S+)/$', graves.views.display_page, name='page'),
    re_path(r'^memorials/(?P<start>\S+)/(?P<end>\S+)$', graves.views.memorials_list, name='memorials_list'),
]
