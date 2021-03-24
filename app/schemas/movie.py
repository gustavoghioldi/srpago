def schema():
    return {
        'title': {
            'type':'string',
            'required': True,
        },
        'sinopsis' : {
            'type': 'string',
            'required': True
        },

        '3d' : {
            'type': 'boolean',
            'default': False
        },
        'country': {
             'type':'string',
             'required': True,
             'data_relation': {
                 'resource' : 'countries',
                 'field': 'isocode3'
             }
        },
        'duration': {
            'type': 'integer',
            'required': True
        },
        'gender': {
            'type': 'string',
        },
        'pic': {
            'type': 'media'
        },
        'trailer_url': {
            'isurl': True,
            'type': 'string' 
        },
        'metadata':{
            'type': 'dict'
        }
    }