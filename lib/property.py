#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GYSC
# property.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

class Property(object):
    def __init__(self, name, type):
        if not isinstance(name, str):
            raise TypeError("Expected \"name\" to a str object")

        if not isinstance(type, str):
            raise TypeError("Expected \"type\" to a str object")

        self.name = name
        self.type = type

    def __str__(self):
        return name + ": " + type