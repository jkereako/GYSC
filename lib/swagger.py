#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GYSC
# swagger.py
#
# Created by Jeff Kereakoglow on 5/2/19.
# Copyright © 2018 AlexisDigital. All rights reserved.

import json

# http://petstore.swagger.io/v2/swagger.json
class Swagger(object):
    def __init__(self, json_file_path):
        with open(json_file_path) as json_file:
            self.json = json.load(json_file)

    def parse_definitions(self):
        contracts_dict = {"structs": {}, "enums": {}}

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

                    contracts_dict["enums"][swift_type] = enum_cases

                    continue

                if type == "array":
                    if "items" in property:
                        items = property["items"]
                        element_type = ""

                        if "type" in items:
                            element_type = items["type"].capitalize()
                        elif "$ref" in items:
                            element_type = items["$ref"].split("/")[-1].capitalize()

                        swift_type = '[' + element_type + ']'
                        
                if type == "string":
                    swift_type = "String"

                    if "format" in property and property["format"] == "date-time":
                        swift_type = "Date"
                    
                elif type == "integer":
                    swift_type = "Int"

                elif type == "boolean":
                    swift_type = "Bool"

                properties_dict[property_name] = swift_type
        
            contracts_dict["structs"][contract_name] = properties_dict

        return contracts_dict

def main():
    try:
        swagger = Swagger("../temp/swagger.json")
        print(swagger.parse_definitions())

    except ValueError:
        # TODO: Report an error to the Shell script
        print("Failed to parse the JSON file")

if __name__ == "__main__":
    main()