from jsonschema import validate

schema = {
    "type": "object",
    "required": ["first_name" ],
    "properties": {
        "first_name": {
            "type": "string",
            "maxLength": 100
        },
        "last_name": {
            "type": "string",
            "maxLength": 100
        }
    }
};

# If no exception is raised by validate(), the instance is valid.
print(validate(instance={"first_name" : "Doni"}, schema=schema))
# Will throw exception
print(validate(instance={"last_name" : "Rubiagatra"}, schema=schema))

