import os

from auth.account_auth import AccountAuth
from schemas import (
    movie,
    account,
    country,
    cinema,
    calendar,
    )


OPLOG = True
OPLOG_NAME = 'apilog'

DATE_FORMAT="%Y-%m-%dT%H:%M:%S" 

MONGO_URI='mongodb+srv://admin:admn@cluster0.8jlfp.mongodb.net/master?retryWrites=true&w=majority'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

URL_PREFIX='api'
API_VERSION='v1'

IF_MATCH = False

DOMAIN = {
    'countries': {
        'item_title': 'country',
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'public_methods': ['GET'],
        'schema': country.schema()
    },
    'accounts': {
        'item_title':'account',
        'auth_field': 'username',
        'authentication': AccountAuth,
        'schema': account.schema()
    },
    'movies': {
        'item_title':'movie',
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'schema': movie.schema(),
        'public_methods': ['GET']
    },
    'cinemas': {
        'item_title':'cinema',
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'schema': cinema.schema(),
        'public_methods': ['GET']
    },
    'calendar': {
        'item_title':'calendar',
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'schema': calendar.schema(),
        'public_methods': ['GET']
    }
}
