
# list => array(배열)과 비슷한 역할
# arry(배열)의 특징 : 고정길이 : 특징이자 단점, "메모리에 연속적인 할당 : 배열의 장점"

test_list = list()
print(test_list, type(test_list)) # 생성자

test_list = []  # 기호로 표현
print(test_list, type(test_list))

# 대괄호에 문자가 있으면 무조건 리스트

test_list = [1, 2, 3]
print(test_list)


# 다른 타입을 넣어도 됨
test_list = ["김민재", 22, 173]
print(test_list)

for data in test_list:
    print(data)

# p.193
stu_1 = [20230001, "김인하", "컴정", 20]
stu_2 = [20230010, "이인하", "컴시", 21]

print("학번")

print(stu_1[0])
print(stu_2[0])

print("이름")

print(stu_1[1])
print(stu_2[1])

stu_1[0] = 20230002
print(stu_1[0])

# 20230010 학생의 성(family name)을 출력하세요.
print(stu_2[1][0]) # == "이인하" => "이"

# stu_1 학생의 입학년도 출력
print(str(stu_1[0])[0:4])

