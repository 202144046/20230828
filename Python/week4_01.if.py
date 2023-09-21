reg_number = input("주민등록번호 : ")
gender_number = int(reg_number[6])

# 남자인지 판별하는 if문 작성해보자

if gender_number == 1 or gender_number == 3 or gender_number == 5 or gender_number == 7:
    print("남성")

if gender_number == 2 or gender_number == 4 or gender_number == 6 or gender_number == 8:
    print("여성")

if gender_number in "1357":
    print("남자")

if gender_number % 2 == 1:
    print("남자")

number = int(input("정수:"))

if number > 0:
    print("양수")

if number < 0:
    print("음수")

if number == 0:
    print("0")

