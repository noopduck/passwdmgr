from typing import List
from typing import Dict

class JsonBlob():
    def __init__(self, user, sites: Dict):
        self.user = user
        self.sites = sites

class User():
    def __init__(self, user):
        self.user = user

class Sites():
    def __init__(self, user, password, date):
        self.user = user
        self.password = password
        self.date = date

