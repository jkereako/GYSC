#!/usr/bin/env python
#
# GYSC
# gysc.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

import json

# http://petstore.swagger.io/v2/swagger.json
class Parser(object):
    def __init__(self, json):
        self.json = json

    def parse2(self):
        definitions = self.json["definition"]

        for contract_name in definitions.keys():
            contract = definitions[contract_name]
            properties = contract["properties"]

            for property_name in properties.keys():
                property = properties[property_name]
                type = property["type"]
                swift_type = ""

                try:
                    for case in  property["enum"]:
                        print(case)
                except:
                    pass

                if type == "string":
                    try:
                        if property["format"] == "date-time":
                            swift_type = "Date"
                    except:
                        swift_type = "String"

                elif type == "integer":
                    swift_type = "Integer"

                elif type == "boolean":
                    swift_type = "Boolean"
               
    def parse(self):
        # path: /pet/findByStatus
        for path in self.json["paths"]:
            # http_method: get
            for http_method in path:
                # response: 404
                for response in http_method["responses"]:
                    try:
                        for item in response["schema"]["items"]:
                            # xpath: #/definitions/Pet
                            xpath = item["$ref"]
                            definition = self.xpath_query(xpath)
                            self.parse_definition(definition)
                    except:
                        pass

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