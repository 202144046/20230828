# 1st = a, 2nd = b, 3rd = c, avg = d

print("1st:", end='')
a = int(input())

print("2nd:", end='')
b = int(input())

print("3rd:", end='')
c = int(input())

d = (a + b + c)/3

d = round(d, 2)

print(a , end='')
print("," , end='')
print(b , end='')
print("," , end='')
print(c , end='')
print("의 평균은" , end=' ')
print(d , end='')
print("입니다." , end='')
