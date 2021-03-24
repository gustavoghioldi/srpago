from werkzeug.exceptions import Unauthorized, UnprocessableEntity
import base64
from environment import (SU_USERNAME, SU_PASSWORD)
class AccountHelper:
    @staticmethod
    def hide_password(response):
        if response.get('_items'):
            for item in response["_items"]:
                del (item['password'])
        else:
            del (response['password'])
    
    @staticmethod
    def verify_create_account(request, other=None):
        if 'admin' in request.json.get("roles"):
            if not (request.authorization['username'] == SU_USERNAME and request.authorization['password'] == SU_PASSWORD):
                raise Unauthorized(description="Only superuser can create admin users")
        if 'user' in request.json.get("roles"):
            if request.authorization['username'] != request.json['username'] or request.authorization['password'] != request.json['password']:
                raise UnprocessableEntity(description='basic authorization header values must be the same as the body (username | password)') 
            
    @classmethod
    def add_ticket(updates, original):
        if updates.get('tickets'):
            if len(updates.get('tickets'))>1:
                raise Unauthorized(description='You dont autorized to add more than 1 tickets at time')
            calendars = app.data.driver.db['calendar']
            calendar = calendars.find_one({'_id':ObjectId(updates['tickets'][0])})
            if calendar['tickets']<= 0:
                raise UnprocessableEntity(description="there are no more tickets")

            calendars.update_one({"_id":ObjectId(updates['tickets'][0])}, {"$set": {"tickets":calendar['tickets'] -1}})
            updates['tickets'] = updates['tickets'] + original['tickets']
        