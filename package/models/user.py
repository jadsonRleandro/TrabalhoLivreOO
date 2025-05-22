class user:
    def __init__(self, name, password, record = 0):
        self.name = name
        self.password = password
        self.record = record

    def toDic(self):
        us = {'name': self.name, 'password': self.password, 'record': self.record}
        return us