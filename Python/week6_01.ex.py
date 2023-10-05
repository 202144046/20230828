
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

