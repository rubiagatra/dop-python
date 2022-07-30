request_schema = {
    "type": "object",
    "required": ["first_name"],
    "properties": {
        "first_name": {
            "type": "string",
            "maxLength": 100
        },
    },
};

search_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "first_name", "last_name"],
        "properties": {
            "id": {
                "type": "integer"
            },
            "first_name": {
                "type": "string",
                "maxLength": 100
            },
            "last_name": {
                "type": "string",
                "maxLength": 100
            }
        },
    }
};


response_schema = {
    "type": "object",
    "required": ["first_name", "last_name"],
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

