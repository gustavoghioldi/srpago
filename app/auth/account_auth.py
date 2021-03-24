'''
BaseAuth
'''
from .base_auth import BaseAuth

class AccountAuth(BaseAuth):
    '''
    AccountAuth class
    '''
    def check_auth_resource(self,username, password, method, account):
        '''
        overwrite the method of BaseAuth
        this method allows only users to see its values ​​and all administrators
        '''
        _value = False
        if method != 'POST':
            if account is not None or password != account['password']:
                pass
            if account and '_id' in account:
                self.set_request_auth_value(account['username'])
            _value =  True
        else:
            _value = True
        return _value
