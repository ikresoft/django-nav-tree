from django.conf.urls import patterns, url
from views import form_view

urlpatterns = patterns('',
	url(r'^form_view/$', form_view, name='form_view'),
)