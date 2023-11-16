a = 1
b = 1
c = 1

def vartest1(a):
    a = a + 1

def vartest2(b):
    b = b + 1
    return b

def vartest3():
    # global c   # 주석처리하면..?
    c = c + 1    # 전역변수를 사용하고 싶으면 global 쓰기

vartest1(a)
b = vartest2(b)
vartest3()
print(a,b,c)    # 1 2 2

