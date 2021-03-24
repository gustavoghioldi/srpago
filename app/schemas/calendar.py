def schema():
    return {
        'cinema': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'cinemas',
                'field': '_id',
                'embeddable': True
            }
        },
        'datetime': {
            'type': 'datetime',
            'required': True
        },
        'movie': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'movies',
                'field': '_id',
                'embeddable': True
            }
        },
        'tickets': {
            'type': 'integer',
            'default': 0
        }
    }