def schema():
    return {
    "isocode3": {
        "type":"string",
        "minlength": 3,
        "maxlength": 3,
        "required": True,
        "unique": True
    },
    "name": {
        "type":"string",
        "minlength": 3,
        "maxlength": 36,
        "required": True,
        "unique":True
    },
    "metadata": {
        'type': 'dict'
    }
}