from django.conf.urls import url
from rango import views

urlpatterns = [

    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='category'),
	url(r'', views.index, name = 'show_category'),
]