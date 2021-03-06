#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Toran Sahu <toran.sahu@yahoo.com>
#
# Distributed under terms of the MIT license.

"""

"""

from .views import SchemeViewSet, make_request, load_data, TicketViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


app_name = 'dep1'

router = DefaultRouter()
router.register('schemes', SchemeViewSet, base_name='schemes')
router.register('tickets', TicketViewSet, 'tickets')

urlpatterns = router.urls

urlpatterns += [path('request/', make_request, name='sumbit-request')]
urlpatterns += [path('load-data/', load_data, name='load-data')]
