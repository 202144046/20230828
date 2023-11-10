

# 열고
# f = open("c:\\test_b\\test01.txt", 'w') # 새로운 걸 만들땐 w, 기존에 있을때 새로 추가하고 싶으면 a
f = open("c:\\test_b\\test01.txt", 'a') # 새로운 걸 만들땐 w, 기존에 있을 때 내용을 새로 추가하고 싶으면 a

# 작업
# print(f)
f.write("김인하\n")
f.write("컴퓨터정보과\n")
f.write("1학년\n")

f.write("이인하|컴퓨터시스템과|2학년\n")

# 닫고
f.close()

try:
    pass
except:
    print("폴더가 없나?")

