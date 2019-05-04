#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GYSC
# struct.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

from contract import Contract

class Struct(Contract):
    def __init__(self, name, properties):
        if type(name) is not str:
            raise TypeError("Expected \"name\" to be a str object")

        if not isinstance(properties, list):
            raise TypeError("Expected \"properties\" to be a list")

        Contract.__init__(self, name)

        self.properties = properties