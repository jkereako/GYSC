#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GYSC
# enum.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

from contract import Contract

class Enum(Contract):
    def __init__(self, name, backing_type, cases):
        if type(backing_type) is not str:
            raise TypeError("Expected \"type\" to be a str object")

        if not isinstance(cases, list):
            raise TypeError("Expected \"properties\" to be a list")
        
        Contract.__init__(self, name)

        self.backing_type = backing_type
        self.cases = cases