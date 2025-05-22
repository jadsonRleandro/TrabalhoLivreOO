from package.models.windowModel import Gui, label
from package.dataBaseControler import dataBase
from package.models.user import user

class leaderGui(Gui):
    def __init__(self, us):
        super().__init__(440, 800, "Menu")
        self.user = us
        self.record = self.getRecord(self.user)
        self.styles = {
            'recordStyle': """
                QLabel{
                    font-size: 25px;
                    color: red;
                }
            """,
            'leaderStyle': """
                QLabel{
                    font-size: 20px;
                    color: white;
                }
            """
        }
        
        self._top5 = [{'name': "None", 'record': 0},{'name': "None", 'record': 0},{'name': "None", 'record': 0},{'name': "None", 'record': 0},{'name': "None", 'record': 0}]
        self.recordLabel = label(f"Record: {self.record}", self.gui,30, 80, self.styles['recordStyle'])
        label(f"{self.user['name']}", self.gui, 30, 30, self.styles['recordStyle'])
        label("Ranking", self.gui, 160, 130, "font-size:30px; color:'white';")
        self.top1 = label(f"1. {self._top5[0]['name']} ---------- {self._top5[0]['record']}", self.gui, 30, 200, self.styles['leaderStyle'])
        self.top2 = label(f"2. {self._top5[1]['name']} ---------- {self._top5[1]['record']}", self.gui, 30, 250, self.styles['leaderStyle'])
        self.top3 = label(f"3. {self._top5[2]['name']} ---------- {self._top5[2]['record']}", self.gui, 30, 300, self.styles['leaderStyle'])
        self.top4 = label(f"4. {self._top5[3]['name']} ---------- {self._top5[3]['record']}", self.gui, 30, 350, self.styles['leaderStyle'])
        self.top5 = label(f"5. {self._top5[4]['name']} ---------- {self._top5[4]['record']}", self.gui, 30, 400, self.styles['leaderStyle'])

    def modify(self):
        self.record = self.getRecord(self.user)
        self.recordLabel.modifyTxt(f"Record: {self.record}", self.width, 30)
        self.top1.modifyTxt(f"1. {self._top5[0]['name']} ---------- {self._top5[0]['record']}", self.width, 30)
        self.top2.modifyTxt(f"2. {self._top5[1]['name']} ---------- {self._top5[1]['record']}", self.width, 30)
        self.top3.modifyTxt(f"3. {self._top5[2]['name']} ---------- {self._top5[2]['record']}", self.width, 30)
        self.top4.modifyTxt(f"4. {self._top5[3]['name']} ---------- {self._top5[3]['record']}", self.width, 30)
        self.top5.modifyTxt(f"5. {self._top5[4]['name']} ---------- {self._top5[4]['record']}", self.width, 30)

    
    def ranking(self):
        records = dataBase.getRecords()
        records.sort(key=lambda rec: rec['record'])
        i = 0
        while i < 5:
            l = len(records) - 1
            if l - i == -1:
                i = 5
            else:
                self._top5[i] = records[l - i]
            i += 1
        self.modify()
    
    @classmethod
    def getRecord(cls, us):
        use = dataBase.verindataB(user(us['name'], us['password']))
        return use['record']