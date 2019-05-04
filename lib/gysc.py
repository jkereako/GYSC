#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GYSC
# gysc.py
#
# Created by Jeff Kereakoglow on 8/31/18.
# Copyright © 2018 AlexisDigital. All rights reserved.

import json

# http://petstore.swagger.io/v2/swagger.json
class Swagger(object):
    def __init__(self, json):
        self.json = json

    def parse_definitions(self):
        contracts_dict = {}

        definitions = self.json["definitions"]
        
        for contract_name in definitions.keys():
            properties_dict = {}
            contract = definitions[contract_name]
            properties = contract["properties"]

            for property_name in properties.keys():
                swift_type = ""

                property = properties[property_name]
                
                # Is this property a reference to an object?
                if "$ref" in property:
                    swift_type = property["$ref"].split("/")[-1]
                    
                    properties_dict[property_name] = swift_type
                    continue

                # If not, then this property will have a type
                type = property["type"]

                # Is this property an enum?
                if "enum" in property:
                    # Make up the contract name for the enum
                    swift_type = contract_name.capitalize() + property_name.capitalize()

                    # Declare the type
                    properties_dict[property_name] = swift_type

                    # Define the cases
                    enum_cases = {}
                    for case in property["enum"]:
                        enum_cases[case] = type

                    contracts_dict[swift_type] = enum_cases

                    continue

                if type == "string":
                    try:
                        if property["format"] == "date-time":
                            swift_type = "Date"
                    except:
                        swift_type = "String"

                elif type == "integer":
                    swift_type = "Int"

                elif type == "boolean":
                    swift_type = "Bool"

                properties_dict[property_name] = swift_type
        
            contracts_dict[contract_name] = properties_dict

        return contracts_dict

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
    with open("../temp/swagger.json") as json_file:
        json_data  = json.load(json_file)
        swagger = Swagger(json_data)
        print(swagger.parse_definitions())

        # try:
        #     json_data  = json.load(json_file)
        #     swagger = Swagger(json_data)

        # except ValueError:
        #     # TODO: Report an error to the Shell script
        #     print("Failed to parse the JSON file")

if __name__ == "__main__":
    main()