# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from envelope.views import ContactView


urlpatterns = patterns('',
    url(r'^$', ContactView.as_view(), name='envelope-contact'),
)

