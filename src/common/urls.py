#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Toran Sahu <toran.sahu@yahoo.com>
#
# Distributed under terms of the MIT license.

"""

"""

from .views import NotificationViewSet, get_tx_data
from rest_framework.routers import DefaultRouter
from django.urls import path, include


app_name = 'common'

get_by_dep_view = NotificationViewSet.as_view({'get':'get_by_dep'})
urlpatterns = [path('dep/<slug:dep>/', get_by_dep_view)]

router = DefaultRouter()
router.register('notifications', NotificationViewSet, base_name='notifications')

urlpatterns += router.urls

urlpatterns += [path('tx-data/', get_tx_data, name='tx-data'),]
