# p.251

scores = [100, 45, 80, 0, 23]

print(min(scores))
print(max(scores))
print(sum(scores))
print(sum(scores)/len(scores)) # 정수형 나누기

# 사용자가 입력한 점수를 가지고
# 평균을 구하는 코드를 작성하세요.

print("\n")

# p.252

scores = [100, 45, 80, 0, 23]
print(reversed(scores))
print(list(reversed(scores)))
print(scores)

a = reversed(scores) # reversd는 주로 1회성
for r in a:
    print("1st", r)
for r in a:
    print("2nd", r)

print("\n")

# p.254

# enumerate()의 결과는 tuple의 형태

scores = [100, 45, 80, 0, 23]
for i, score in enumerate("김민재"):
    print(f"{i+1}번 과목:{score}")

for i, score in enumerate(scores):
    print(f"{i+1}번 과목:{score}")

print()
print()
print()
print()

print("\n")

# p.256 - items()는 dict 메소드라고 생각하면 된다.

example = {1: "one", 2: "two", 5: "five"}

for k in example:
    print(k)

for k in example.keys(): # 정통적인 방법
    print(k)

for v in example.values():
    print(v)

for k, v in example.items():
    print(k, v)

print("\n")

# p.263 - join()

fruits = ["딸기", "사과", "배"]

my_fav = "" # 타 프로그래밍 언어
for f in fruits:
    if len(my_fav) > 0:
        my_fav += ","
    my_fav += f

print(my_fav)

print("," .join(fruits)) # 파이썬

print("\n")

# p.257 리스트 내포

array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)
print()

array = [ i * i for i in range (0, 20, 2) ]

array = []
for i in range(0, 20, 2):
    if i % 4:
        array.append(i * i)
print(array)
print()

array = [i * i for i in range(0, 20, 2) if i % 4]

print("\n")

# 연습 문제

ip_addr = [127, 0, 0, 1] # "127.0.0.1"
ip_addr_neu = [str(ip) for ip in ip_addr]

ip_addr = "." .join(ip_addr_neu)
print(ip_addr)

