
name = input("이름:")
age = int(input("나이:"))

print("이름:" + name + "나이:" + str(age))

print("나의 이름은 ", name, "이고 나이는 ", age, "세 입니다.", sep="")

# " " : 공백 문자열
# "" : 빈 문자열

intro = "이름:name 나이:age"
print(intro)
print(end="\n\n\n")

# 방법 1 - 전통적인 방식
intro = "이름:%s 나이:%d" % (name, age)
print(intro)
print(end="\n\n\n")

# 방법 2 - 요즘 많이 쓰는 방식
intro = "이름:{} 나이:{}" .format(name, age)
print(intro)
print(end="\n\n\n")

intro = "이름:{1} 나이:{0}" .format(name, age) # 인덱스 번호로 순서 바꾸기 가능
print(intro)
print(end="\n\n\n")

# 방법 3 - 보간법, f-string
intro = f"이름:{name} 나이:{age+1}"
print(intro)
print(end="\n\n\n")





strip

upper
lower

in 연산자

"#" 스플릿 파일처리 할 때 중요

| 파이프 쪼개지는 갯수 => split은 무조건 리스트로 쪼개짐 즉 [] 대괄호 안에 있음.

datetime now

sort => 오름차순, 기본값은 sort(reversed=False)
sort(reversed=True) => 내림차순(큰 수부터)

# p.207

test_list = [1, 2, 3, 20, 22]

# 향상된 for문, foreach문 = for-in문

for element in test_list:
    print(element)

for element in "컴퓨터정보과":
    print(element)

딕셔너리 공부하기

