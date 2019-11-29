import re
import hashlib


class CreateUser:

    def __init__(self, first_name, last_name, addresses, phones, password, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self.first_name = first_name
        self.last_name = last_name
        self.addresses = self.check_addresses(addresses)
        self.phones = self.check_phones(phones)
        self.password = self.hash_password(password)

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def hash_password(self, password):
        hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
        return hashed_password

    def __getattribute__(self, item):
        if item.startswith('pass'):
            raise AttributeError('AccessDeniedError')
        # return object.__getattribute__(self,item)
        return super().__getattribute__(item)

    def check_addresses(self, addresses):
        c_list = ["country", "city", "index", "billing_address",]
        for a in addresses:
            if not all([key in a.keys() for key in c_list]):
                raise ValueError("Not valid address data")
            else:
                return addresses

    def check_phones(self, phones):
        if isinstance(phones, list) and len(phones) <= 3:
            for elem in phones:
                elem = re.sub(r'[^0-9.]+', r'', str(elem))
                if len(str(elem)) > 15:
                    raise Exception("Wrong number")
            return phones
        else:
            raise Exception("More then 3 numbers")


billing_ad = [
    {"country": "Ukraine", "city": "Kharkiv", "index": 61195, "billing_address": "St. "},
]

user1 = CreateUser(first_name="Alice", last_name="Black", phones=[555357595, 5555555, 666], password="password",
                   addresses=billing_ad)

print(user1.first_name)
print(user1.last_name)
print(user1.fullname())
print(user1.phones)
# print(user1.password)  # !
print(user1.addresses)
