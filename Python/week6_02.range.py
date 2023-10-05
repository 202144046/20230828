
# 함수나 메소드를 잘 기억하자!

# range = range(10)
# print(range, type(range))
# range = range(5)
# print(range)

# list = [1, 2, 3]
# a = list("Aaaa")

# range_test1 = range(10)
# range_test2 = range(2, 10)
# range_test3 = range(2, 10, 3)

range_test1 = list(range(10))
range_test2 = list(range(2, 10))
range_test3 = list(range(2, 10, 3))

print(range_test1)
print(range_test2)
print(range_test3)

for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(5, 10, 3):
    print(i)

# p.234
fruits = ["딸기", "귤", "키위", "복숭아"]

for fruit in fruits:
    print(fruit)
print()

for i in range(4):
    print(f"{i+1} 순위 {fruits[i]}")
    print()

for i in range(len(fruits)):
    print(f"{i+1} 순위 {fruits[i]}")
    print()

for i in reversed(range(len(fruits))):
    print(f"{i+1} 순위 {fruits[i]}")
    print()

scores = [10,20,30,20]
max_score = scores[0]
for i in range(1, len(scores)):
    if max_score < scores[i]:
        max_score = scores[i]

max_score = max(scores)

