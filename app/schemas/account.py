def schema():
    return {
    'first_name': {
        'type':'string',
        'minlength': 3,
        'maxlength': 36,
        'required': True,
    },
    'last_name': {
        'type':'string',
        'minlength': 3,
        'maxlength': 36,
        'required': True,
    },
    'username': {
        'type':'string',
        'minlength': 3,
        'maxlength': 156,
        'required': True,
        'unique':True
    },
    'password': {
        'type':'string',
        'minlength':6,
        'maxlength':36,
        'required': True
    },
    'roles': {
        'type': 'list',
          'allowed': ['user', 'admin'],
          'required': True
    },
    'tickets': {
        'type': 'list',
        'data_relation': {
            'resource': 'calendar',
            'field': '_id',
            'embeddable': True
        }
    }
}