'''
Principal file
Practico Sr Pago
'''
import logging

from eve import Eve
from flask import request

from auth.base_auth import BaseAuth
from helpers.account_helper import AccountHelper
from custom_validations import CustomValidator

app=Eve(auth=BaseAuth, validator=CustomValidator)

@app.before_request
def before_request():
    ''' logging all requests'''
    app.logger.info(request)
@app.after_request
def after_request(response):
    ''' logging all responses'''
    app.logger.info(response)
    return response
app.on_fetched_resource_accounts += AccountHelper.hide_password
app.on_fetched_item_accounts     += AccountHelper.hide_password
app.on_update_accounts           += AccountHelper.add_ticket
app.on_pre_POST_accounts         += AccountHelper.verify_create_account

if __name__ == "__main__":
    handler = logging.getLogger()
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=3600)
