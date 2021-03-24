from eve.io.mongo import Validator
import validators

class CustomValidator(Validator):
    def _validate_isurl(self, url, field, value):
        if url and not validators.url(value):
            self._error(field, 'it must be a url for example http://youtube.com')
    def _validate_isemail(self, url, field, value):
        pass
