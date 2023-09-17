# a = 투입한 돈, b = 물건의 가격, c = 거스름 돈

a = int(input("투입한 돈:"))
b = int(input("물건의 가격:"))

c = a - b

print("거스름 돈:", end='')
print(c)

d = c // 500

print("500 동전 개수:", end='')
print(d)

e = d % 100
print("100 동전 개수:", end='')
print(e)
