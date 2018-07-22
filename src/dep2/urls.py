#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Toran Sahu <toran.sahu@yahoo.com>
#
# Distributed under terms of the MIT license.

"""

"""

from .views import SchemeViewSet, make_response
from rest_framework.routers import DefaultRouter
from django.urls import path, include


app_name = 'dep2'

router = DefaultRouter()
router.register('schemes', SchemeViewSet, base_name='schemes')

urlpatterns = router.urls

urlpatterns += [path('approve/', make_response, name='approve-request')]
