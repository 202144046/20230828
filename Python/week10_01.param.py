# p.279 기본(값) 매개변수

print("장은미", end="\t") # 기본값 매개변수 end="\n"
print("4x", "인하", "공업", sep="\n")


# 기본값 매개변수 선언은 뒤쪽에...

def intro(name, grade):
    print(f"나는 {name}이고, {grade}학년이야")

# def intro(grade=1, name):
#     print(f"나는 {name}이고, {grade}학년이야")

# def intro(hobby, grade=1, name):
#     print(f"나는 {name}이고, {grade}학년이야")

# intro("장은미") # 오류
intro("장은미", 3)

# p.280 키워드 매개변수

def intro(name, grade="1", hobby="없음"):
    print(f"{name}")
    print(f"{grade}")
    print(f"{hobby}")

intro("장은미")
intro("장은미", "없다")
intro("장은미", hobby="게임")
intro(name="장은미", hobby="게임")
intro(hobby="게임", name="장은미")
# intro(hobby="게임", grade=2) # 기본 매개변수가 없으면 매개변수를 넣어줘야 한다.

# 가변인자(*args)
# 가변키워드인자(**kargs)

# p.278 가변매개변수

# *args(가변인자)

def intro(name, grade, *hobbies):   # keypoints : *(별표시)
    print(type(hobbies))
    print(name, grade)
    if 0 < len(hobbies):
        print(", ".join(hobbies))
    else:
        print(hobbies)
        print("없다")

intro("김인하", 1)
intro("김인하", 1, "디아블러 4", "카트라이더", "삼국지", "대항해시대")

