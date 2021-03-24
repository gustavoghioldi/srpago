''' app.auth.base_auth'''
from eve.auth import BasicAuth
from flask import current_app
from environment import (SU_PASSWORD, SU_USERNAME)
class BaseAuth(BasicAuth):
    '''BaseAuth is custom of BasicAuth eve class'''
    def check_auth(self, username, password, allowed_roles, resource, method):
        '''check if superuser and if not set account and compare passwords
           is a overwrite of you father class
        '''
        if username == SU_USERNAME and password == SU_PASSWORD:
            return True

        accounts = current_app.data.driver.db['accounts']
        account = accounts.find_one({'username':username})
        if account:
            if 'admin' in account['roles'] and (account['password']==password):
                return True
        return self.check_auth_resource(username, password, method, account)
    def check_auth_resource(self,username, password, method, account)->bool:
        ''' method for customs implements of auth'''
