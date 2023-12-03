# 202144046 김민재

import datetime

class Car:
    def __init__(self, number) -> None:
        self.number = number # 차량번호
        self.intime = datetime.datetime.now() # 입차시간
        self.outtime = None # 출차시간

    def set_out(self): # 출차시 현재 메소드가 호출한 시간으로 출차 시간 설정
        self.outtime = datetime.datetime.now()

    def is_out(self):
        if self.outtime == None:
            return True
        else:
            return False

    def cal_price(self, hour=2000):
        if self.is_out == False:
            TimeGap = self.intime - datetime.datetime.now()
        else:
            TimeGap = self.intime - self.outtime

        TimeSecond = TimeGap.total_seconds()

        pay = (TimeSecond / 3600) * hour

        return pay

    def __str__(self) -> str:
        if self.outtime == None:
            return "주차중"
        
        else:
            outtime_str = self.outtime.strftime('%Y-%m-%d %H:%M:%S')
            return outtime_str
        
    





    