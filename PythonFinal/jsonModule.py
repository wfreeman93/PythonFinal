import json


class Account:
    def __init__(self, account_number="555", first_name="FirstTest", last_name="LastTest", phone_number="999999999",
                 address="123 N Test St"):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address


class AccountJSONEEncoder(json.JSONEncoder):
    def default(self, obj):
        d = dict()
        d["account_number"] = obj.account_number
        d["first_name"] = obj.first_name
        d["last_name"] = obj.last_name
        d["phone_number"] = obj.phone_number
        d["address"] = obj.address
        return d
