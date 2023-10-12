def test():
    print(1)
    print(2)
    # return None 기본 값

print(test()) # None

print("\n")

def test():
    print("3")
    print("4")
    return 0

print(test()) # 0

print("\n")

def test():
    print("5")
    return
    print("6") # 함수는 return을 만나면 호출한 곳으로 돌아감. -> 이후 함수는 작동안함
    return 0

print(test()) # None

print("\n")

def test(itr): # 매개변수 (parameter)
    for i in range(itr):
        print("안녕")

print(test(2))

print("\n")

def test(i): # 매개변수 (parameter)

    for it in range(i):
        print("안녕")

test(2) # 인자 (argument)

print("\n")

def test(n, content):

    for i in range(n):
        print(content)

test(2, "안녕")

print("\n")

def avg(datas):

    if type(datas) is list:
        return sum(datas) / len(datas)

print(avg([1,2,3,4]))
result = avg("1234")

if result:
    print(result)
else:
    print("자료에 문제가 있습니다.")

print("\n")

def calculate_average_from_dict(scores):
    values = list(scores.values())
    return sum(values) / len(values)

student_scores={"김인하":92, "이인하":85, "박인하":78}
avg_score = calculate_average_from_dict(student_scores)
print(f"평균 점수 : {avg_score:.2f}")


