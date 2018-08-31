#!/usr/bin/env python
#
# GYSC
# gysc.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

import json

class Parser(object):
    def __init__(self, json):
        self.json = json

    def parse(self):
        # path: /v1/foo/bar
        for path in self.json["paths"]:
            # http_method: get
            for http_method in path:
                # response: 404
                for response in http_method["responses"]:
                    if "schema" in response:
                        # xpath: #/definitions/FooResponse
                        xpath = response["schema"]["$ref"]

                        definition = self.xpath_query(xpath)
                        self.parse_definition(definition)

    def parse_definition(self, definition):
        for property in definition["properties"]:
            if "$ref" in property:
                xpath = property["$ref"]
                definition = self.xpath_query(xpath)
                self.parse_definition(definition)

    def xpath_query(self, xpath):
        value = self.json

        try:
            for x in xpath.strip("/").split("/"):
                value = value.get(x)
        except:
            pass

        return value

def main():
    with open("swagger.json") as json_file:
        json_data  = json.load(json_file)

        Parse(json_data)

    pprint(data)

if __name__ == "__main__":
    main()