from schema import search_schema
from jsonschema import validate

def search_user(first_name: str):
    if first_name.find("Doni") == 0:
        user = [{
            "id": 1,
            "first_name": "Doni",
            "last_name": "Rubiagatra"
        }]
        validate(user, schema=search_schema)

        return user

    return []
