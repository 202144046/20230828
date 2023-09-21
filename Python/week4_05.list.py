test = ["딸기", "복숭아", "귤", "배", "사과"]

del test[4]
print(test)

del test[0:2]   # del은 슬라이싱 가능
print(test)

test.append("키위")
test.append("거봉")
test.append("블루베리")
print(test)

test.remove # remove는 지운다.

test.pop()  # pop은 뽑아낸다.
test.pop()
test.pop(0)

print(test)

