# rewritten

import hashlib


class CreateUser:

    def __init__(self, first_name, last_name, addresses, phones, password, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self.fullname = self.fullname(first_name, last_name)
        self.__password = self.hash_password(password)

        # self.first_name = first_name
        # self.last_name = last_name
        self.addresses = self.check_addresses(addresses)
        self.phones = self.check_phones(phones)

    @staticmethod
    def fullname(first_name, last_name):
        return f'{first_name} {last_name}'

    @staticmethod
    def hash_password(password):
        hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
        return hashed_password

    def check_password(self, password1):
        if self.__password == self.hash_password(password1):
            return True
        raise Exception("Not relevant")

    @property
    def password(self):
        raise Exception("Hidden data!")

    @password.setter
    def password(self, new_pass):
        self.__password = self.hash_password(new_pass)

    @staticmethod
    def check_addresses(addresses):
        c_list = ["country", "city", "index", "billing_address", ]
        for a in addresses:
            if not all([key in a.keys() for key in c_list]):
                raise ValueError("Not valid address data")
            else:
                return addresses

    @staticmethod
    def check_phones(phones):
        if isinstance(phones, list) and len(phones) <= 3:
            for elem in phones:
                if len(str(elem)) > 15:
                    raise Exception("Wrong number")
            return phones
        else:
            raise Exception("More then 3 numbers")


billing_ad = [
    {"country": "Ukraine", "city": "Kharkiv", "index": 61195, "billing_address": "St. "},
]

user1 = CreateUser(first_name="Alice", last_name="Black", phones=[555357595, 5555555, 666], password="password1",
                   addresses=billing_ad)

# print(user1.first_name)
# print(user1.last_name)
print(user1.fullname)
print(user1.phones)
print(user1._CreateUser__password)  # !
# print(user1.password)
print(user1.check_password(password1="password1"))
print(user1.addresses)
