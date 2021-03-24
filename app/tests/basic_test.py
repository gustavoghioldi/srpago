import unittest
import datetime
from helpers.account_helper import AccountHelper
from bson.objectid import ObjectId

account_helper = AccountHelper()
get_account_response = {'_id': ObjectId('6056682ea225bb09b5ba2431'), 'username': 'gustavoghioldi2', 'first_name': 'Gustavo', 'last_name': 'Ghioldi', 'password': '111111', 'roles': ['user'], '_updated': datetime.datetime(2021, 3, 21, 1, 33, 17), '_created': datetime.datetime(2021, 3, 20, 21, 25, 2), 'tickets': ['6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb', '6055594cc4d6dbb65e0502bb'], '_links': {'self': {'title': 'account', 'href': 'accounts/6056682ea225bb09b5ba2431'}, 'related': {'tickets': [{'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}, {'title': 'calendar', 'href': 'calendar/6055594cc4d6dbb65e0502bb'}]}, 'parent': {'title': 'home', 'href': '/'}, 'collection': {'title': 'accounts', 'href': 'accounts'}}}

class BasicTest(unittest.TestCase):

    def test_hide_password_object(self):
        account_helper.hide_password(get_account_response)
        self.assertEqual(get_account_response.get('password'), None)

    def test_verify_create_account_admin(self):
        pass

    def test_add_ticket(self):
        pass