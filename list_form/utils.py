from pymongo import MongoClient
from datetime import datetime
from itertools import combinations
from backend.settings import DATABASE


def get_db_handle():
    client = MongoClient(host=DATABASE['host'],
                         port=DATABASE['port'],
                         )
    db_handle = client[DATABASE['db_name']]
    return db_handle


class Valid_form:
    def __init__(self, value):
        self.value = value
        self.type_form = self.valid_date()

    def valid_date(self):
        try:
            datetime.strptime(self.value, '%Y-%m-%d')
            return 'date'
        except ValueError:
            try:
                datetime.strptime(self.value, '%d.%m.%Y')
                return 'date'
            except ValueError:
                return self.valid_phone()

    def valid_phone(self):
        if self.value.startswith('+7'):
            phone_number = ''.join(list(self.value[2:]))
            if len(phone_number) == 10 and phone_number.isdigit():
                return 'phone'
            return self.valid_email()

    def valid_email(self):
        email = self.value.split('@', maxsplit=1)
        if len(email) == 2:
            if len(email[1].split('.')) == 2:
                return 'email'
            return 'text'


def find_forms(db, request):
    result = []
    if len(request) == 0:
        pass
    else:
        for count_field_in_find in range(1, len(request)+1):
            iter_find = combinations(request.items(), count_field_in_find)
            iter_find = list(map(lambda x: dict(x), iter_find))
            for comb in iter_find:
                list_form = db.find(comb, {'_id': 0})
                result += list((filter(lambda x: len(x) ==
                               count_field_in_find+1, list_form)))
            return result
