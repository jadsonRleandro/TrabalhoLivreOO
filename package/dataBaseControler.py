import json
from package.models.user import user

class dataBase():
    __dataB = [{}]

    @classmethod
    def load(cls):
        with open("package/db/Datas.json", "r") as arquivo:
            cls.__dataB = json.load(arquivo)

    @classmethod
    def save(cls):
        with open("package/db/Datas.json", "w") as arquivo:
            json.dump(cls.__dataB, arquivo, indent=4)
    
    @classmethod
    def saveInDataBase(cls, toSave):
        ver = cls.verindataB(user(toSave['name'], toSave['password']))

        if ver != False:
            for i in range(len(cls.__dataB)):
                if toSave['name'] == cls.__dataB[i]['name']:
                    cls.__dataB[i] = toSave

        else:
            cls.__dataB.append(toSave)
        
        cls.save()


    @classmethod
    def verindataB(cls,us):
        for i in cls.__dataB:
            if us.name == i.get('name'):
                return i
        
        return False
    
    @classmethod
    def getRecords(cls):
        records = []
        for i in cls.__dataB:
            records.append({'name': i['name'], 'record': i['record']})
        
        return records
    