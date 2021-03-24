def schema():
    return {
        'name': {
            'type':'string',
            'required': True
        },
        'address': {
            'type': 'string',
            'required': True
        },
        'metadata': {
            'type':'dict'
        }
    }