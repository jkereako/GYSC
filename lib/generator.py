#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GYSC
# generator.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

import os
import time
from swagger import Swagger
from enum import Enum
from struct import Struct
from property import Property

# http://petstore.swagger.io/v2/swagger.json
class Generator(object):
    def __init__(self, swagger):
        if type(swagger) is not Swagger:
            raise TypeError("Expected \"swagger\" to be a Swagger object")

        self.swagger = swagger

    def generate(self):
        pass

    def mkdir(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)