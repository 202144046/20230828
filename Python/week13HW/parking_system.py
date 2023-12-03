# 202144046 김민재

import datetime

from car import Car

if __name__ == "__main__":
    car1 = Car("123가 1234")
    car2 = Car("123가 1235")
    print(car1)
    print(car2)
    print("출차" if car1.is_out() else "주차중")
    print("출차" if car2.is_out() else "주차중")

    car2.set_out()
    print(car2)
    print(car2)
    print("출차" if car1.is_out() else "주차중")
    print("출차" if car2.is_out() else "주차중")


    car1.intime -= datetime.timedelta(hours=9)
    car2.outtime -= datetime.timedelta(hours=5)

    print("주차요금:" + str(car2.cal_price(1500)))
    print("주차요금:" + str(car2.cal_price(1500)))

