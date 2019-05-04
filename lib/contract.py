#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GYSC
# contract.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

class Contract(object):
    def __init__(self, name):
        if type(name) is not str:
            raise TypeError("Expected \"name\" to be a str object")
        
        self.name = name
        