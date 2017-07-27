import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *
class SingletonType(type): 
    def __call__(cls, *args, **kwargs): 
        try: 
            return cls.__instance 
        except AttributeError: 
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs) 
            return cls.__instance


class MyWindow(QMainWindow):

    __metaclass__ = SingletonType

    def __init__(self):
        app = QApplication(sys.argv)
        print("init qapplication")
        super().__init__()

        print("qaxwidget")
        # Kiwoom Login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")


    def call_test(self):
        connectresult = self.kiwoom.OnReceiveConditionVer.connect(self.receive_test)
        print(connectresult)
        return 1

    def event_connect(self, err_code):
        if err_code == 0:
            code = "039490"
            self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
            self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
            ret = self.kiwoom.dynamicCall("GetConditionLoad()")
        return 1
            

    def receive_test(self, ret, msg):
        result = self.kiwoom.dynamicCall("GetConditionNameList()")
        print("=========")
        print(result)
        return result
