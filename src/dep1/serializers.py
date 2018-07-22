#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Toran Sahu <toran.sahu@yahoo.com>
#
# Distributed under terms of the MIT license.

"""

"""

from rest_framework import serializers
from .models import Scheme


class SchemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scheme
        fields = '__all__'
